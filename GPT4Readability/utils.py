import os
import re
from urllib.parse import urlparse
from nbconvert import HTMLExporter, MarkdownExporter
import langchain
from langchain.chains import LLMMathChain
from langchain.agents import AgentType, initialize_agent
# from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.base import BaseCallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA, LLMChain
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import TextLoader, NotebookLoader, UnstructuredMarkdownLoader
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.cache import InMemoryCache
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import LlamaCppEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def get_docs(root_dir, include_md):
    docs = []
    
    if include_md == None:
        include_md = False  # By default, don't include Markdown files
        # Check for any .md files in the directory
        for dirpath, _, filenames in os.walk(root_dir):
            if any(file.endswith('.md') for file in filenames):
                user_input = input("Found Markdown files. Do you want to include them? (yes/no): ").strip().lower()
                if user_input == 'yes':
                    include_md = True
                break  # Once you found .md files and got user input, you can break out of loop

    # List of popular file extensions for various programming languages
    extensions = [
        '.py',  # Python
        '.js',  # JavaScript
        '.jsx', # React (JavaScript)
        '.ts',  # TypeScript
        '.tsx', # TypeScript with JSX
        '.java', # Java
        '.c',   # C
        '.cpp', # C++
        '.cs',  # C#
        '.go',  # Go
        '.rb',  # Ruby
        '.php', # PHP
        '.rs',  # Rust
        '.swift', # Swift
        '.m',   # Objective-C
        '.html',# HTML
        '.css', # CSS
        '.scss',# SCSS
        '.kt',  # Kotlin
        '.lua', # Lua
        '.r',   # R
        '.pl',  # Perl
        '.sh',  # Shell Script
        '.scala', # Scala
        '.jl', # Julia
        '.ipynb', # Jupyter Notebook
        # '.md',  # Markdown (for documentation purposes) disabled for now because it could cause issues with simply copying whatever readme is already present
    ]

    if include_md:
        extensions.append('.md')  # Add .md extension if user chose to include

    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)

            if file.endswith(tuple(extensions)) and "/.venv/" not in dirpath:
                try:
                    if file.endswith('.ipynb'):
                        # Convert notebook to Markdown
                        md_exporter = MarkdownExporter()
                        body, resources = md_exporter.from_filename(full_file_path)

                        # Remove images from the markdown content
                        body = re.sub(r'!\[.*?\]\(.*?\)', '', body)

                        md_filename = full_file_path.replace('.ipynb', '.md')
                        
                        # Save the converted notebook as a markdown file
                        with open(md_filename, 'w', encoding='utf-8') as f:
                            f.write(body)

                        # Load the saved markdown using TextLoader
                        loader = UnstructuredMarkdownLoader(md_filename, encoding="utf-8")
                        docs.extend(loader.load())

                        # Delete the saved markdown
                        os.remove(md_filename)

                    else:
                        loader = TextLoader(full_file_path, encoding="utf-8")
                        docs.extend(loader.load_and_split())
                except Exception as e:
                    print(f"Error processing file {full_file_path}: {e}")
                    continue
    if len(docs) == 0:
        readable_files = [
            "Python",
            "JavaScript & React (JSX)",
            "TypeScript & TypeScript with JSX",
            "Java",
            "C & C++",
            "C#",
            "Go",
            "Ruby",
            "PHP",
            "Rust",
            "Swift",
            "Objective-C",
            "HTML, CSS, & SCSS",
            "Kotlin",
            "Lua",
            "R",
            "Perl",
            "Shell Script",
            "Scala",
            "Julia",
            "Jupyter Notebook (experimental)"
        ]
        
        if include_md:
            readable_files.append("markdown")

        raise ValueError(f"GPT4Readability did not find any files that it can read within the provided directory. The readable files are: {', '.join(readable_files)}.")

    return docs


def get_function_name(code):
    """
    Extract function name from a line beginning with "def "
    """
    if not code.startswith("def ") or "(" not in code:
        raise ValueError("Invalid function definition format")
    return code[len("def "): code.index("(")]


def find_python_files(directory):
    python_files = []
    
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                python_files.append(os.path.join(dirpath, filename))
                
    return python_files

def get_until_no_space(all_lines, i) -> str:
    """
    Get all lines until a line outside the function definition is found.
    """
    ret = [all_lines[i]]
    for j in range(i + 1, i + 10000):
        if j < len(all_lines):
            if len(all_lines[j]) == 0 or all_lines[j][0] in [" ", "\t"]:
                ret.append(all_lines[j])
            else:
                break
        else:  # Added this else clause to handle the end of file scenario
            break
    return "\n".join(ret)

def get_functions(filepath):
    """
    Get all functions in a Python file.
    """
    with open(filepath, 'r') as file:
        whole_code = file.read().replace("\r", "\n")
    all_lines = whole_code.split("\n")
    for i, l in enumerate(all_lines):
        if l.startswith("def "):
            code = get_until_no_space(all_lines, i)
            function_name = get_function_name(code)
            yield {"code": code, "function_name": function_name, "filepath": filepath}


def check_files_in_directory(directory):
    """Check if a directory contains license file or requirements.txt file and identify license type"""
    
    license_exists = False
    requirements_exists = False
    license_filenames = ['license', 'license.txt', 'license.md']
    license_type = None

    for file in os.listdir(directory):
        if file.lower() in license_filenames:
            license_exists = True
            with open(os.path.join(directory, file), 'r') as f:
                content = f.read().lower()
                if 'mit' in content:
                    license_type = 'MIT License'
                elif 'apache' in content:
                    license_type = 'Apache License'
                elif 'gnu general public license' in content or 'gpl' in content:
                    license_type = 'GNU GPL'
        elif file.lower() == 'requirements.txt':
            requirements_exists = True

    result = '\n'
    
    if license_exists and license_type:
        result += f"There is a {license_type} in the directory. "
    elif license_exists:
        result += "There is a license file in the directory but its type could not be determined. "
    else:
        result += "There is no license file in the directory. DO NOT bring up a license file in the readme."
    
    result += "\n"
    if requirements_exists:
        result += "There is a requirements.txt file in the directory."
    else:
        result += "There is no requirements.txt file in the directory.  Do not bring up a requirements file in the readme."
        
    return result

def check_special_files(directory):
    """Check if a directory contains a code of conduct or style guide"""
    
    code_of_conduct_exists = False
    style_guide_exists = False
    code_of_conduct_path = None
    style_guide_path = None

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower() == 'code_of_conduct.md':
                code_of_conduct_exists = True
                code_of_conduct_path = os.path.join(root, file)
            elif file.lower() == 'style_guide.md':
                style_guide_exists = True
                style_guide_path = os.path.join(root, file)

    result = '\n'
    
    if code_of_conduct_exists:
        result += f"A code of conduct exists at the following path: {code_of_conduct_path}. "
    else:
        result += "There is no code of conduct in the directory. \n\nDO NOT bring up a code of conduct in the readme."
    
    result += "\n"
    
    if style_guide_exists:
        result += f"A style guide exists at the following path: {style_guide_path}."
    else:
        result += "There is no style guide in the directory.  \n\nDO NOT bring up a style guide in the readme."
        
    return result

def split_docs(docs):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(docs)
    return texts


def makeEmbeddings(chunked_docs, model_type="gpt"):
    if "gpt" in model_type:
        # Create embeddings and store them in a FAISS vector store
        embedder = OpenAIEmbeddings(disallowed_special=())
    else:
        langchain.llm_cache = InMemoryCache()
        # # this is what was used to create embeddings for the book
        embedder = HuggingFaceInstructEmbeddings(
            embed_instruction="Represent the code repository for retrieval: ",
            query_instruction="Represent the question for retrieving supporting code from the code repository: "
            )

    vector_store = FAISS.from_documents(chunked_docs, embedder)
    return vector_store

def askQs(vector_store, chain, q):
    # Ask a question using the QA chain
    similar_docs = vector_store.similarity_search(q)
    resp = chain.run(input_documents=similar_docs, question=q) # .run
    return resp 

def process_segment(chain, vector_store, segment_prompt, previous_context="", additional_info=""):
    # Include previous context in the current prompt
    full_prompt = "context:  " + previous_context + "\n\n" + "Important information to keep in mind:  " + additional_info + "\n" + segment_prompt 
    response = askQs(vector_store, chain, full_prompt)
    return response.strip()

def loadLLM(model, weights=None, processing_unit=None, config=None):
    if "gpt" in model:
        llm = ChatOpenAI(temperature=0, model=model)
    else:
        callback_manager = BaseCallbackManager([StreamingStdOutCallbackHandler()])
        # Update the model path as per your system
        if processing_unit=="CPU":
            llm = LlamaCpp(
                model_path=weights,
                temperature=config["temperature"],
                max_tokens=config["max_tokens"],
                # repeat_penalty=2.2,
                n_ctx=config["n_ctx"],
                top_p=config["top_p"],
                callback_manager=callback_manager,
                verbose=config["verbose"],
            )
        elif processing_unit=="NVIDIA":
            llm = LlamaCpp(
                model_path=weights,
                temperature=config["temperature"],
                max_tokens=config["max_tokens"],
                # repeat_penalty=2.2,
                n_ctx=config["n_ctx"],
                top_p=config["top_p"],
                n_batch=config["n_batch"],
                # n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance (leaving default for now)
                n_gpu_layers=config["n_gpu_layers"],         # The number of layers to offload to GPU, if you have GPU acceleration available
                callback_manager=callback_manager,
                verbose=config["verbose"],
            )
        elif processing_unit=="Metal":
            llm = LlamaCpp(
                model_path=weights,
                temperature=config["temperature"],
                max_tokens=config["max_tokens"],
                # repeat_penalty=2.2,
                n_ctx=config["n_ctx"],
                top_p=config["top_p"],
                n_batch=config["n_batch"],
                f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
                # n_threads=8,            # The number of CPU threads to use, tailor to your system and the resulting performance (leaving default for now)
                n_gpu_layers=config["n_gpu_layers"],         # The number of layers to offload to GPU, if you have GPU acceleration available
                callback_manager=callback_manager,
                verbose=config["verbose"],
            )
    chain = load_qa_chain(llm, chain_type="stuff")
    return chain


def get_github_info_from_local_repo(repo_path):
    # Path to the config file
    git_config_path = os.path.join(repo_path, ".git", "config")

    # Read the config file
    with open(git_config_path, "r") as file:
        lines = file.readlines()

    # Find the line that starts with 'url ='
    for line in lines:
        if line.startswith("\turl ="):
            # Remove 'url =' and strip whitespace
            url = line.replace("\turl =", "").strip()

            # Use the urlparse function to parse the URL
            result = urlparse(url)

            if "github.com" not in result.netloc and "github.com" not in result.path:
                raise ValueError("URL provided is not a GitHub URL")

            path_parts = result.path.strip("/").lstrip(':').split("/")

            if len(path_parts) < 2:
                raise ValueError("Invalid GitHub URL. Cannot extract username and repository name.")

            username, repo_name = path_parts[0], path_parts[1].replace('.git', '')
            return username, repo_name

    return None, None

def remove_line_with_pattern_from_string(input_string):
    pattern = "[username]/[repo_name]"
    lines = input_string.splitlines()
    lines_without_pattern = [line for line in lines if pattern not in line]
    return '\n'.join(lines_without_pattern)