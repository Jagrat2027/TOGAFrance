"""
generate-pdf.py

Convert Markdown files into styled PDF documents using a configurable engine (WeasyPrint, Pandoc, etc.).
"""

import argparse

def convert_markdown_to_pdf(input_path, output_path, config_path=None):
    # TODO: Load config
    # TODO: Convert MD to HTML
    # TODO: Render to PDF using selected engine
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown to PDF")
    parser.add_argument("--input", required=True, help="Path to the Markdown file or folder")
    parser.add_argument("--output", required=True, help="Path to output PDF or directory")
    parser.add_argument("--config", help="Path to config.yaml (optional)")
    args = parser.parse_args()

    convert_markdown_to_pdf(args.input, args.output, args.config)
