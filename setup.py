from setuptools import setup, find_packages

with open('README.md', 'r') as readme:
    # ignore gifs
    description = ''.join([i for i in readme.readlines()
                           if not i.startswith('![')])

setup(
    name='GPT4Readability',
    version='0.1.5',
    url='https://github.com/loevlie/GPT4Readability',
    author='Dennis Johan Loevlie',
    author_email='loevliedenny@gmail.com',
    description='A tool to automatically generate a README.md and suggest code improvements for any code repository.  It uses GPT-3, GPT-4, or an optional LocalAI model to generate the README.md and suggestions.',
    long_description=description,
    long_description_content_type='text/markdown',
    packages=find_packages(),  # automatically discover all packages and subpackages
    include_package_data=True,     
    package_data={"GPT4Readability": ["prompts/*.txt"]},
    python_requires='>=3.6',
    install_requires= [
        "langchain",
        "openai",
        "faiss-cpu",
        "tiktoken",
        "click",
        "tqdm",
        "unstructured",
        "markdown",
        "nbconvert",
        "typer[all]",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': [
            'gpt4readability=GPT4Readability.__main__:app',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
