import os
import typer
from typing import Optional
from typing_extensions import Annotated
from getpass import getpass
from GPT4Readability.readme_gen import generate_readme
from GPT4Readability.suggestions_gen import generate_suggestions


app = typer.Typer()

@app.command()
def main(
    path: str,
    function: Annotated[str, typer.Option("--function", "-f",help="Function to use: 'readme', 'suggestions', or 'both'")] = "readme",
    output_readme: Annotated[str, typer.Option("--output-readme", "-or",help='Output filename for readme')] = "README_Generated.md",
    output_suggestions: Annotated[str, typer.Option("--output-suggestions", "-os", help='Output filename for suggestions')] = "suggestions.md",
    model: Annotated[str, typer.Option("--model", "-m",help='Model to use. Possible models: "gpt-3.5-turbo", "gpt-4", "local"')] = "gpt-3.5-turbo",
    include_md: Annotated[Optional[bool], typer.Option(help='Whether to include .md files')] = None,
    weights: Annotated[Optional[str], typer.Option("--weights", "-w",help='Path to weights file for the localAI model')] = None,
    processing_unit: Annotated[Optional[str], typer.Option("--processing-unit", "-pu",help='Processing unit to use (CPU, NVIDIA, Metal)')] = None
):
    """CLI tool for GPT4Readability."""

    if not os.getenv('OPENAI_API_KEY') and model not in ['local', 'mixtral_8x7b']:
        print("OPENAI_API_KEY environment variable not found. Please input it:")
        os.environ['OPENAI_API_KEY'] = getpass()

    if not output_readme.endswith('.md'):
        output_readme += '.md'
    
    if not output_suggestions.endswith('.md'):
        output_suggestions += '.md'

    if 'readme' in function or 'both' in function:
        print(f"\n[INFO] Commencing README generation using {model}.")
        generate_readme(path, output_readme, model, include_md, weights=weights, processing_unit=processing_unit)
        print(f"\n[SUCCESS] README generated at: {os.path.join(path, output_readme)}\n")
    
    if 'suggestions' in function or 'both' in function:
        generate_suggestions(path, output_suggestions, model)

if __name__ == "__main__":
    typer.run(main)
