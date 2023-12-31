# This is the README file GPT4Readability (version 0.0.7) made for itself around mid July using GPT-3.5-turbo

# GPT4Readability

[![License Badge](https://img.shields.io/github/license/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/loevlie/GPT4Readability)](https://github.com/loevlie/GPT4Readability/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

GPT4Readability is a powerful tool designed to automatically generate a comprehensive README.md file and suggest code improvements for any Python code repository. With its advanced AI capabilities, GPT4Readability goes beyond surface-level interpretation, allowing it to establish connections between disparate parts of code and gain an in-depth understanding of the code's functionality, structure, and intent.  

> Other than this sentence this readme file and this [suggestions file](https://github.com/loevlie/GPT4Readability/blob/main/suggestions.md) were both generated by GPT4Readability using gpt-3.5-turbo.  Any other changes made will be listed below:

* I added the version (0.0.7) to the installation section.
* UPDATE: README generation (suggestions coming soon!) is now integrated into [Huggingface Spaces 🤗](https://huggingface.co/spaces) using [Gradio](https://github.com/gradio-app/gradio). Try out the Web Demo: [![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/JohanDL/GPT4Readability)

## Features

- Automatic generation of a detailed README.md file for your Python codebase
- Suggestions for code improvements to enhance readability and maintainability

## Installation

To use GPT4Readability, you need to have Python 3.6 or higher installed on your system. You can install GPT4Readability and its dependencies using the following command:

```shell
pip install GPT4Readability==0.0.7
```

## Usage

GPT4Readability provides two main functionalities: README generation and code improvement suggestions. You can choose to use either one or both of these functions.

### README Generation

To generate a README.md file for your codebase, use the following command:

```bash
gpt4readability <path> --function readme --output_readme README.md --model <model>
```

Replace `<path>` with the path to your codebase directory and `<model>` with the desired model to use (either "gpt-3.5-turbo" or "gpt-4").

### Code Improvement Suggestions

To generate code improvement suggestions for your codebase, use the following command:

```bash
gpt4readability <path> --function suggestions --output_suggestions suggestions.md --model <model>
```

Replace `<path>` with the path to your codebase directory and `<model>` with the desired model to use (either "gpt-3.5-turbo" or "gpt-4").

## Authors

GPT4Readability is developed and maintained by Dennis Johan Loevlie. For any inquiries or support, please contact Dennis Johan Loevlie at loevliedenny@gmail.com.

## Contributing

Contributions to GPT4Readability are welcome! If you encounter any issues or have suggestions for improvements, please report them by opening an issue on the [GitHub repository](https://github.com/loevlie/GPT4Readability/issues).

To contribute code changes, follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the main branch.
3. Make your desired changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request on the main repository.

Please ensure that your code changes adhere to the coding style and guidelines of the project.

## Support

For support or assistance with using GPT4Readability, please contact Dennis Johan Loevlie at loevliedenny@gmail.com.

## License

GPT4Readability is licensed under the MIT License. See the [LICENSE](https://github.com/loevlie/GPT4Readability/blob/main/LICENSE) file for more details.