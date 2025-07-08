"""
tf-assistant.py

Command-line tool to interact with a local AI assistant trained to write in the TOGAFrance style.
"""

def ask(prompt, language="fr"):
    # TODO: Call OpenAI, local LLM, or load prompt templates
    pass

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--language", default="fr")
    args = parser.parse_args()

    ask(args.prompt, args.language)
