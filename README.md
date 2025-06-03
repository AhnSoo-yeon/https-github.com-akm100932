# MetaGPT Client

This repository provides a simple command-line client for interacting with the MetaGPT API using the `openai` Python library.

## Setup

1. Create a virtual environment (optional).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set the `OPENAI_API_KEY` environment variable with your API key.

## Usage

Run the client and pass the prompt as an argument:

```bash
python metagpt_client.py "Hello MetaGPT"
```

The script prints the response from the MetaGPT API.

