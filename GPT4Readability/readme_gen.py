import os
from getpass import getpass
from GPT4Readability.utils import *
import importlib.resources as pkg_resources  


def generate_readme(root_dir, output_name, model):
    """Generates a README.md file based on the python files in the provided directory

    Args:
        root_dir (str): The root directory of the python package to parse and generate a readme for
    """

    # prompt_folder_name = os.path.join(os.path.dirname(__file__), "prompts")
    # prompt_path = os.path.join(prompt_folder_name, "readme_prompt.txt")

    with pkg_resources.open_text('GPT4Readability.prompts','readme_prompt.txt') as f:         
		inb_msg = f.read()

    # with open(prompt_path) as f:
    #     lines = f.readlines()
    # inb_msg = "".join(lines)

    file_check_result = check_files_in_directory(root_dir) # Checking for the license and requirements.txt
    inb_msg += file_check_result
    special_file_check_result = check_special_files(root_dir) # Checking for the code of conduct and the style guide
    inb_msg += special_file_check_result

    username, reponame = get_github_info_from_local_repo(root_dir)

    if username:
        inb_msg = inb_msg.replace("[username]", username.replace("git@github.com:",""))
        inb_msg = inb_msg.replace("[repo_name]", reponame.replace(".git",""))
    else:
        inb_msg = remove_line_with_pattern_from_string(inb_msg)


    docs = get_docs(root_dir)
    texts = split_docs(docs)
    if len(texts) > 8300: # For now this is roughly the size we can accept
       LOCAL_resp = 'The GitHub repository is too large (I am working on getting this working with larger repositories)'
    else:
        chain = loadLLM(model)
        LOCAL_vector_store = makeEmbeddings(texts)
        LOCAL_resp = askQs(LOCAL_vector_store, chain, inb_msg)

    # Write the string to the README.md file
    with open(os.path.join(root_dir,output_name), 'w') as f:
        f.write(LOCAL_resp)