# Badges
[![License Badge](https://img.shields.io/github/license/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE)

# Introduction
GPT4Readability is a powerful tool designed to automatically generate README documentation for any code repository. It utilizes advanced AI models, such as GPT-3 and GPT-4, to understand the structure and content of the codebase, and then generates a comprehensive, engaging, and accurate README file.

GPT4Readability is designed to save developers time and effort when creating README documentation for their code repositories. By automating this process, GPT4Readability ensures that the README files generated for code repositories are of high quality, accurate, comprehensive, engaging, and easy to understand.

In summary, GPT4Readability is an advanced AI tool designed to automatically generate high-quality README documentation for any code repository. By leveraging the power of advanced AI models, such as GPT-3 and GPT-4, GPT4Readability ensures that the README files generated for code repositories are of the highest quality, accurate, comprehensive, engaging, and easy to understand.
To install GPT4Readability, follow these steps:

1. **Clone the repository:**
   Open a terminal and run the following command to clone the GPT4Readability repository:
   ```
   git clone https://github.com/loevlie/GPT4Readability.git
   ```
2. **Navigate to the cloned repository:**
   Run the following command to navigate to the cloned GPT4Readability repository:
   ```
   cd GPT4Readability
   ```
3. **Install the required dependencies:**
   Before running GPT4Readability, you need to install the required dependencies. To do this, run the following command:
   ```
   pip install -r requirements.txt
   ```
4. **Run GPT4Readability:**
   After completing the previous steps, you can now run GPT4Readability. To do this, simply run the following command:
   ```
   python gpt4readability.py
   ```
That's it! You have successfully installed and run GPT4Readability. If you encounter any issues or have any questions, feel free to reach out to the GPT4Readability team for assistance.
To run GPT4Readability, you need to install several dependencies. Here's a list of the required dependencies and their roles in the project:

1. **langchain**: This library provides tools for building applications with large language models. In GPT4Readability, langchain is used to load and manage the language model.

2. **openai**: This library provides a Python interface for the OpenAI API. In GPT4Readability, openai is used to interact with the OpenAI API and load the language model.

3. **faiss-cpu**: This library provides tools for efficient similarity search and clustering of dense vectors. In GPT4Readability, faiss-cpu is used to perform efficient similarity search and clustering of the dense vectors representing the code snippets in the repository.

4. **tiktoken**: This library provides tools for encoding and decoding text into subword token sequences using various tokenization algorithms. In GPT4Readability, tiktoken is used to encode and decode the text in the code snippets in the repository into subword token sequences using the Byte-Pair Encoding (BPE) tokenization algorithm.

5. **click**: This library provides tools for building command line interfaces (CLIs) in Python. In GPT4Readability, click is used to build the CLI for interacting with the tool and generating the README.md file for the repository.

6. **tqdm**: This library provides tools for adding a progress bar to long-running tasks in Python. In GPT4Readability, tqdm is used to add a progress bar to the long-running task of generating the README.md file for the repository using the tool.

7. **markdown**: This library provides tools for parsing and rendering Markdown text into HTML in Python. In GPT4Readability, markdown is used to parse and render the Markdown text in the code snippets in the repository into HTML when generating the README.md file for the repository using the tool.

8. **nbconvert**: This library provides tools for converting Jupyter Notebook files (.ipynb) into various formats, including HTML, LaTeX/PDF, Markdown, reStructuredText, and AsciiDoc in Python. In GPT4Readability, nbconvert is used to convert the generated README.md file for the repository into an HTML format when generating the final output of the tool for the user to view and interact with the generated README.md file for the repository in a web browser using the HTML format.

9. **typer[all]**: This library provides tools for building command line interfaces (CLIs) in Python with advanced features, such as type hints, subcommands, context variables, plugins, and extensions. In GPT4Readability, typer is used to build the CLI for interacting with the tool and generating the README.md file for the repository using the tool with advanced features, such as type hints, subcommands, context variables, plugins, and extensions.

10. **pyyaml**: This library provides tools for parsing and rendering YAML text into Python data structures and vice versa in Python. In GPT4Readability, pyyaml is used to parse and render the YAML text in the code snippets in the repository into Python data structures when generating the README.md file for the repository using the tool with advanced features, such as type hints, subcommands, context variables, plugins, and extensions.

That's it! You have now successfully listed and explained the dependencies required for GPT4Readability with their roles in the project.
Here are some practical examples of how to use GPT4Readability:

1. **Generate a README file for your code repository:**

    ```bash
    gpt4readability generate-readme /path/to/your/code/repository --model "gpt-3.5-turbo" --output-readme "/path/to/your/generated/README.md"
    ```

    This command will generate a README file for your code repository using the specified model (in this case, `gpt-3.5-turbo`). The generated README file will be saved to the specified output path (in this case, `/path/to/your/generated/README.md`)).

2. **Generate suggestions for improving your code:**

    ```bash
    gpt4readability generate-suggestions /path/to/your/code/repository --model "gpt-3.5-turbo" --output-suggestions "/path/to/your/generated/suggestions.md"
    ```

    This command will generate suggestions for improving your code using the specified model (in this case, `gpt-3.5-turbo`)). The generated suggestions will be saved to the specified output path (in this case, `/path/to/your/generated/suggestions.md`)).

Please note that these are just examples and you may need to modify them based on your specific use case and environment. Additionally, please make sure to replace any placeholders or example values with the actual paths, filenames, and other relevant details for your specific use case and environment.
Thank you for your interest in contributing to GPT4Readability! We welcome contributions from anyone in the community. Here's a guide on how to contribute to GPT4Readability.

**Submitting Pull Requests**

1. Fork the repository on GitHub.
2. Clone the forked repository to your local machine.
3. Create a new branch from the `main` branch for your changes.
4. Make your changes in the new branch.
5. Once you've made all your changes, commit them to your branch.
6. Push your changes to your fork on GitHub.
7. Create a pull request from your fork to the original repository on GitHub.

**Reporting Bugs**

If you find a bug in GPT4Readability, please follow these steps to report it:

1. Open an issue on the GPT4Readability repository on GitHub.
2. Provide a clear and concise description of the bug, including any error messages that you received.
3. Explain how to reproduce the bug, including any specific steps or inputs that are required.
4. If possible, provide a proposed solution or workaround for the bug.
5. Add any relevant labels or tags to the issue, such as "bug" or "enhancement".
6. Assign the issue to yourself or to a relevant team member, if applicable.
7. Submit the issue and wait for a response from the GPT4Readability team.

**Code of Conduct**

Please note that all contributors to GPT4Readability are expected to adhere to our Code of Conduct, which can be found in the repository's `CODE_OF_CONDUCT.md` file.

Thank you for your contributions to GPT4Readability! We appreciate your help in making our project better for everyone in the community.
The authors and maintainers of GPT4Readability are as follows:

1. Dennis Johan Loevlie (djloevlie@gmail.com): Dennis is the main author and maintainer of GPT4Readability. He has contributed to all aspects of the project, including design, development, testing, documentation, deployment, maintenance, support, and user experience.

2. [Your Name Here] ([your-email@example.com](mailto:your-email@example.com))): [Your Bio Here] has also contributed to GPT4Readability. Their specific contributions are detailed below:

* Contribution 1: [Describe the contribution in detail.]
* Contribution 2: [Describe the contribution in detail.]
* Contribution 3: [Describe the contribution in detail.]

[Your Bio Here] is grateful for the opportunity to contribute to GPT4Readability. They are committed to continuing to support the project and its community of users.
To generate a README.md file for your project, you can use the `generate_readme` function provided by the GPT4Readability library. Here's an example of how to use this function:
```python
from GPT4Readability.readme_gen import generate_readme

# Set up the parameters for the generate_readme function
root_dir = "/path/to/your/project/directory"
output_name = "README"  # The name of the output README.md file
model = "gpt-3.5-turbo"  # The model to use for generating the README.md file
include_md = False  # Whether or not to include existing markdown files in the generated README.md file
weights=None, processing_unit=None

# Generate the README.md file using the generate_readme function
generate_readme(root_dir, output_name, model, include_md,weights=weights, processing_unit=processing_unit)
```
In this example, we first import the `generate_readme` function from the GPT4Readability library. We then set up the parameters for the `generate_readme` function, including the path to the project directory, the name of the output README.md file, the model to use for generating the README.md file, whether or not to include existing markdown files in the generated README.md file, and any additional weights or processing units to use for the model.

Once we have set up these parameters, we can then call the `generate_readme` function with these parameters to generate the README.md file for our project.
