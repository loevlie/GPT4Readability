from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings.openai import OpenAIEmbeddings
import os
from langchain.chains import RetrievalQA
from langchain import LLMMathChain
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool, tool
from urllib.parse import urlparse

def get_docs(root_dir):
    docs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith((".py", ".html")) and "/.venv/" not in dirpath:
                try:
                    loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
                    docs.extend(loader.load_and_split())
                except Exception as e:
                    pass
    return docs

def get_function_name(code):
    """
    Extract function name from a line beginning with "def "
    """
    assert code.startswith("def ")
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
    whole_code = open(filepath).read().replace("\r", "\n")
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


def makeEmbeddings(chunked_docs):
    # Create embeddings and store them in a FAISS vector store
    embedder = OpenAIEmbeddings(disallowed_special=())
    vector_store = FAISS.from_documents(chunked_docs, embedder)
    return vector_store

def askQs(vector_store, chain, q):
    # Ask a question using the QA chain
    similar_docs = vector_store.similarity_search(q)
    resp = chain.run(input_documents=similar_docs, question=q) # .run
    return resp 

def loadLLM(model):
    llm = ChatOpenAI(temperature=0, model=model)
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