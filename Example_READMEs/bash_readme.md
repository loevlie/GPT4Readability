# GPT4Readability generated README for [git-secret](https://github.com/sobolevn/git-secret/tree/master) using GPT-3.5-turbo

# git-secret

[![License Badge](https://img.shields.io/github/license/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

git-secret is a tool that allows you to store sensitive information securely within a git repository. It encrypts files and directories, making them inaccessible to unauthorized users. This ensures that sensitive data, such as passwords or API keys, remains protected even if the repository is compromised.

## Functionalities

- Add files to be hidden
- Decrypt and print the contents of a file
- Check if a file has changed since the last commit
- Delete all encrypted files
- Encrypt or re-encrypt files to be hidden
- Initialize the git-secret repository
- Remove a person's public key from the keyring
- List all added files
- Remove files from the list of hidden files
- Decrypt all hidden files
- Import a person's public key into the keyring
- Print usage information
- Print list of authorized email addresses

## Installation

To install git-secret, follow these steps:

1. Clone the git-secret repository:

   ```shell
   git clone https://github.com/sobolevn/git-secret.git
   ```

2. Change into the cloned directory:

   ```shell
   cd git-secret
   ```

3. Run the installation script for your package manager:

   - For Debian-based systems:

     ```shell
     sudo ./utils/deb/install.sh
     ```

   - For RPM-based systems:

     ```shell
     sudo ./utils/rpm/install.sh
     ```

   - For Alpine Linux:

     ```shell
     sudo ./utils/apk/install.sh
     ```

## Dependencies

git-secret has the following dependencies:

- GnuPG
- Bash
- Git

Make sure these dependencies are installed on your system before using git-secret.

## Usage

To use git-secret, you can run the following commands:

- `git secret add [file.txt]`: Adds a file to be hidden.
- `git secret cat [file.txt]`: Decrypts and prints the contents of a file.
- `git secret changes [file.txt.secret]`: Indicates if the file has changed since the last commit.
- `git secret clean`: Deletes all encrypted files.
- `git secret hide`: Encrypts or re-encrypts the files to be hidden.
- `git secret init`: Initializes the git-secret repository.
- `git secret removeperson [emails]`: Deletes a person's public key from the keyring.
- `git secret list`: Prints all the added files.
- `git secret remove [files]`: Removes files from the list of hidden files.
- `git secret reveal`: Decrypts all hidden files.
- `git secret tell [email]`: Imports a person's public key into the keyring.
- `git secret usage`: Prints the usage message.
- `git secret whoknows`: Prints the list of authorized email addresses.

For more information about each command and their options, you can use the `git secret [command] -h` command.

## Authors

git-secret is maintained by [sobolevn](https://github.com/sobolevn).

## Contributing

Contributions to git-secret are welcome! If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/sobolevn/git-secret/issues) on the GitHub repository.

Before contributing, please make sure to read and adhere to the [code of conduct](./vendor/bats-core/docs/CODE_OF_CONDUCT.md).

## Support

If you need support or have any questions, you can reach out to the maintainers of git-secret by [opening an issue](https://github.com/sobolevn/git-secret/issues) on the GitHub repository.

For commercial support, please contact the maintainers directly.

## License

git-secret is licensed under the [MIT License](https://github.com/sobolevn/git-secret/blob/main/LICENSE).

# GPT4Readability generated README for [git-secret](https://github.com/sobolevn/git-secret/tree/master) using GPT-4

# Git-Secret

[![License Badge](https://img.shields.io/github/license/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/sobolevn/git-secret)](https://github.com/sobolevn/git-secret/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Welcome to the Git-Secret repository! This codebase is designed to manage and securely store your sensitive information within a Git repository. 

## Table of Contents
- [Purpose and Functionalities](#purpose-and-functionalities)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [Support](#support)

## Purpose and Functionalities

Git-Secret is a bash tool that allows you to store your sensitive data inside your repository. It encrypts tracked files with public keys for users whom you trust using gpg, allowing secrets to be shared securely. 

Here are some of the main functionalities:

- **Add**: Adds a file to be hidden to the list.
- **Cat**: Decrypts and prints contents of the file.
- **Changes**: Indicates if the file changed since the last commit.
- **Clean**: Deletes all encrypted files.
- **Hide**: Encrypts (or re-encrypts) the files to be hidden.
- **Init**: Initializes the git-secret repository.
- **Removeperson**: Deletes a person's public key from the keyring.
- **List**: Prints all the added files.
- **Remove**: Removes files from the list of hidden files.
- **Reveal**: Decrypts all hidden files.
- **Tell**: Imports a person's public key into the keyring.
- **Usage**: Prints this message.
- **Whoknows**: Prints list of authorized email addresses.

## Installation

The installation scripts for different platforms are located in the `utils` directory. You can find scripts for Debian-based systems (`install-deb.sh`), RPM-based systems (`install-rpm.sh`), and Alpine Linux (`install-apk.sh`). 

To install, navigate to the `utils` directory and run the appropriate script for your system. For example, on a Debian-based system, you would run:

```bash
cd utils/deb
./install.sh
```

## Dependencies

This codebase does not have a `requirements.txt` file, as it is primarily a bash tool. However, it does require `gpg` (GNU Privacy Guard) to encrypt and decrypt files.

## Usage

Here is an example of how to use some of the main functionalities:

```bash
# Initialize the git-secret repository
git secret init

# Add a file to be hidden
git secret add file.txt

# Encrypt the file
git secret hide

# Decrypt the file
git secret reveal
```

## Contributing

We welcome contributions from the community! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes in your branch.
4. Submit a pull request with your changes.

Please make sure to follow our [Code of Conduct](./vendor/bats-core/docs/CODE_OF_CONDUCT.md) when contributing.

## Support

If you need support, have a question, or want to report a bug, please open an issue on our [GitHub issues page](https://github.com/sobolevn/git-secret/issues).

For commercial support, please email the maintainer directly.

## Authors and Maintainers

This project is maintained by [sobolevn](https://github.com/sobolevn). 

## Donations

If you find this project useful and want to support its development, please consider making a donation. You can email the maintainer directly for details on how to donate.

Thank you for your interest in Git-Secret! :grinning: