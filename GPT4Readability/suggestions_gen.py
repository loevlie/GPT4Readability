import os
from getpass import getpass
from GPT4Readability.utils import *
from tqdm import tqdm 

def generate_suggestions(root_dir, output_name, model):
    """Generates a suggestions.md file with suggested improvements to the code based on the python files in the provided directory

    Args:
        root_dir (str): The root directory of the python package to parse and generate a readme for
    """

    prompt_folder_name = os.path.join(os.path.dirname(__file__), "prompts")
    prompt_path = os.path.join(prompt_folder_name, "refactor_prompt.txt")

    with open(prompt_path) as f:
        lines = f.readlines()
    inb_msg = "".join(lines)

    docs = get_docs(root_dir)
    python_files = find_python_files(root_dir)
    suggestions = []
    
    texts = split_docs(docs)
    chain = loadLLM(model)
    LOCAL_vector_store = makeEmbeddings(texts)
    for doc in tqdm(python_files, desc="Optimizing the code"):
        for func in tqdm(get_functions(doc),desc="Optimizing functions",leave=False):
            LOCAL_resp = askQs(LOCAL_vector_store, chain, inb_msg.replace("[INSERT FUNCTION HERE]",func['code']))

            if "NO CHANGES NEEDED" in LOCAL_resp:
                continue 
            else:
                out = f"\nfilepath: {func['filepath']}\n\nfunction_name: {func['function_name']}\n\noriginal function: \n```python\n{func['code']}\n```\n\nsuggestion: \n{LOCAL_resp}"
                print(out)
                suggestions.append(out)



    # Write the string to the README.md file
    with open(os.path.join(root_dir,output_name), 'w') as f:
        f.write("\n=========================================\n".join(suggestions))