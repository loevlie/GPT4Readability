# GPT4Readability

[![License Badge](https://img.shields.io/github/license/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Welcome to **GPT4Readability**! This tool is designed to automatically generate a README.md and suggest code improvements for any code repository. It uses GPT-3, GPT-4, or an optional LocalAI model to generate the README.md and suggestions. 

> Other than this sentence this readme file and this [suggestions file](https://github.com/loevlie/GPT4Readability/blob/main/suggestions.md) were both generated by GPT4Readability using gpt-3.5-turbo.  Any other changes made will be listed below:

* I added the version (0.1.5) to the installation section.
* UPDATE: README generation (suggestions coming soon!) is now integrated into [Huggingface Spaces 🤗](https://huggingface.co/spaces) using [Gradio](https://github.com/gradio-app/gradio). Try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/JohanDL/GPT4Readability)
* I recently got access to GPT-4 so the GPT-4 version of the gpt4readability README can be found here [GPT-4_Example](https://github.com/loevlie/GPT4Readability/blob/main/Example_READMEs/gpt4readability_gpt4_readme.md)
* The README file generation works with all programing languages but for now the code suggestions is still python only. 
* The new local AI is Mixtral-8x7b, this was setup using llamacpp and langchain.  The installation process can be found [here](https://python.langchain.com/docs/integrations/llms/llamacpp) and you should be able to download any gguf model to try but the ones I found work well can be downloaded from [here](https://huggingface.co/TheBloke/Mixtral-8x7B-Instruct-v0.1-GGUF/blob/main/mixtral-8x7b-instruct-v0.1.Q4_K_M.gguf)!  A config file for the model setup is located at `GPT4Readability/configs/local_ai.yaml` and an example of the local AI results can be found in [this README](https://github.com/loevlie/GPT4Readability/blob/main/Example_READMEs/Local_AI_Readme.md).

## Main Functionalities :grinning:

- **README Generation**: Automatically generates a comprehensive README.md for your code repository.
- **Code Improvement Suggestions**: Provides suggestions for improving your code.
- **Support for Multiple Models**: Supports GPT-3, GPT-4, and LocalAI models.
- **Large Repository Support**: Capable of handling repositories of up to 8300 text segments.

## Installation :sweat_smile:

GPT4Readability requires Python 3.6 or higher. You can install it using pip:

```bash
pip install GPT4Readability==0.1.5
```

## Dependencies :innocent:

The following packages are required:

- langchain
- openai
- faiss-cpu
- tiktoken
- click
- tqdm
- unstructured
- markdown
- nbconvert
- typer[all]
- pyyaml

You can install all dependencies using pip:

```bash
pip install langchain openai faiss-cpu tiktoken click tqdm unstructured markdown nbconvert typer[all] pyyaml langchain_openai
```

## Usage :smiley:

You can use GPT4Readability as a command-line tool. Here's an example:

```bash
gpt4readability --function readme --output-readme README_Generated.md --model gpt-3.5-turbo
```

This command will generate a README for the current directory using the GPT-3.5-turbo model and save it as README_Generated.md.

## Contributing :fire:

We welcome contributions! Here's how you can help:

- **Reporting Bugs**: If you find a bug, please [open an issue](https://github.com/loevlie/GPT4Readability/issues) on GitHub.
- **Pull Requests**: If you've fixed a bug or added a new feature, we'd love to see your work! Please [submit a pull request](https://github.com/loevlie/GPT4Readability/pulls).
- **Donations**: If you find this tool useful and would like to support its development, you can make a donation. Please email the author for details.

## Author :blush:

GPT4Readability is developed by Dennis Johan Loevlie. You can contact him at loevliedenny@gmail.com.

## Support :zap:

For commercial support, please contact the author at loevliedenny@gmail.com.

## License :open_file_folder:

GPT4Readability is licensed under the MIT License. You can view the license [here](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE).

Thank you for using GPT4Readability! We hope you find it useful.
