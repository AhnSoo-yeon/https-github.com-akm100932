import os
import openai


def call_metagpt(prompt: str) -> str:
    """Send a prompt to the MetaGPT API and return the response text."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("Set the OPENAI_API_KEY environment variable")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace with 'MetaGPT' if available
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"].strip()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Call the MetaGPT API")
    parser.add_argument("prompt", help="Prompt text to send to MetaGPT")
    args = parser.parse_args()
    print(call_metagpt(args.prompt))

