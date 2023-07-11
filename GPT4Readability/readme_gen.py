import os
from getpass import getpass
from GPT4Readability.utils import *

def generate_readme(root_dir, output_name, model):
    """Generates a README.md file based on the python files in the provided directory

    Args:
        root_dir (str): The root directory of the python package to parse and generate a readme for
    """

    prompt_folder_name = os.path.join(os.path.dirname(__file__), "prompts")
    prompt_path = os.path.join(prompt_folder_name, "readme_prompt.txt")

    with open(prompt_path) as f:
        lines = f.readlines()
    inb_msg = "".join(lines)

    file_check_result = check_files_in_directory(root_dir) # Checking for the license and requirements.txt
    inb_msg += file_check_result
    special_file_check_result = check_special_files(root_dir) # Checking for the code of conduct and the style guide
    inb_msg += special_file_check_result

    username, reponame = get_github_info(root_dir)
    inb_msg = inb_msg.replace("[username]", username)
    inb_msg = inb_msg.replace("[repo_name]", reponame)


    docs = get_docs(root_dir)
    texts = split_docs(docs)
    chain = loadLLM(model)
    LOCAL_vector_store = makeEmbeddings(texts)
    LOCAL_resp = askQs(LOCAL_vector_store, chain, inb_msg)

    # Write the string to the README.md file
    with open(os.path.join(root_dir,output_name), 'w') as f:
        f.write(LOCAL_resp)