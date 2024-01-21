import os
from getpass import getpass
from GPT4Readability.utils import *
import importlib.resources as pkg_resources  
from tqdm import tqdm
import yaml

def generate_readme(root_dir, output_name, model, include_md,weights=None, processing_unit=None):
    """Generates a README.md file based on the python files in the provided directory

    Args:
        root_dir (str): The root directory of the python package to parse and generate a readme for
    """
    if "gpt" in model:
        print(model)
        with pkg_resources.open_text('GPT4Readability.prompts','readme_prompt.txt') as f:         
            inb_msg = f.read()
            config = None
    else:
        with pkg_resources.open_text('GPT4Readability.prompts','readme_prompt_open.txt') as f: 
            inb_msg = f.read()
        with pkg_resources.open_text('GPT4Readability.configs','local_ai.yaml') as f: 
            config = yaml.safe_load(f)
            if 'model_path' in config and weights==None:
                weights = config['model_path']
            elif 'model_path' not in config and weights==None:
                raise Exception("You must provide a weights file for the localAI model!")
            if 'processing_unit' in config and processing_unit==None:
                processing_unit = config['processing_unit']
            elif 'processing_unit' not in config and processing_unit==None:
                raise Exception("You must provide a processing unit for the localAI model!")

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


    docs = get_docs(root_dir, include_md)
    texts = split_docs(docs)
    if len(texts) > 8300: # For now this is roughly the size we can accept
       LOCAL_resp = 'The GitHub repository is too large (I am working on getting this working with larger repositories)'
    else:
        chain = loadLLM(model, weights=weights, processing_unit=processing_unit, config=config)
        LOCAL_vector_store = makeEmbeddings(texts, model)
        if "gpt" in model:
            LOCAL_resp = askQs(LOCAL_vector_store, chain, inb_msg)
        elif "local" in model or "mixtral" in model:
            prompt_segments = inb_msg.split('&&&&&&&&&&')
            readme_content = ""
            previous_context = ""
            num = len(prompt_segments)
            start = 0
            for segment in tqdm(prompt_segments, desc="Generating README", leave=False, colour="green"):
                if start == num - 1:
                    additional_info = "Keep the your output EXTREMELY SHORT, accurate, eye catching, fun, and informative and (if applicable) include bullet points, tables, code blocks and headings when needed and trying to stay away from long blocks of text!  Start your output with a short heading that describes the section you are writing about."
                else:
                    additional_info = "Keep the your output EXTREMELY short, accurate, eye catching, fun, and informative including bullet points, tables, code blocks and headings when needed and trying to stay away from long blocks of text!  Remember that this is just one segment of the README so keep it short, no one wants to read a long README but everyone wants a good README!  Start your output with a short heading that describes the section you are writing about.  For example, if you are writing about the installation process, start your output with a heading like '# Installation' or '# How to Install' and use markdown headers with # or ## or ###.  If you are writing about the usage of the code, start your output with a heading like 'Usage' or 'How to Use'.  If you are writing about the license of the code, start your output with a heading like 'License' or 'Code License'.  If you are writing about the contributing guidelines of the code, start your output with a heading like 'Contributing' or 'How to Contribute'."
                segment_response = process_segment(chain, LOCAL_vector_store, segment, previous_context, additional_info=additional_info)
                readme_content += segment_response + "\n"
                previous_context = segment_response  # Update context for next segment
                start += 1
            
            additional_info = "Now I want you clean this readme up.  You NEED to take the previous context I gave you, that should represent the readme file for this repository, and I need you to shorten it and make it more precise and eye catching.  You're main goal is to make this readme much less verbose and remove any lines that may not be true or needed!  Do NOT change wording only remove extra, unnecessary lines!!.  Make this the best README you can!"
            segment_response = process_segment(chain, LOCAL_vector_store, segment, readme_content, additional_info=additional_info)
            readme_content_total = segment_response
            LOCAL_resp = readme_content_total
            with open(os.path.join(root_dir,"segmented_"+output_name), 'w') as f:
                f.write(readme_content)
            print("\n\nDone!\n\n")

    # Write the string to the README.md file
    with open(os.path.join(root_dir,output_name), 'w') as f:
        f.write(LOCAL_resp)