from setuptools import setup, find_packages

setup(
    name='GPT4Readability',
    version='0.0.1',
    url='https://github.com/loevlie/GPT4Readability',
    author='Dennis Johan Loevlie',
    author_email='loevliedenny@gmail.com',
    description='A tool to automatically generate a README.md and suggest code improvements for any python code repository',
    packages=find_packages(),  # automatically discover all packages and subpackages
    python_requires='>=3.6',
    install_requires= [
        "langchain",
        "openai",
        "faiss-cpu",
        "tiktoken",
        "click",
        "tqdm"
    ],
    entry_points={
        'console_scripts': [
            'gpt4readability=GPT4Readability.__main__:main',
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
