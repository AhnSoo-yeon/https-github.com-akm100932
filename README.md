# MetaGPT Client

This repository provides a simple command-line client for interacting with the MetaGPT API using the `openai` Python library.

## Setup

1. Create a virtual environment (optional).
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

# Model Context Protocol (MCP) Server

A FastAPI server exposing a JSON-RPC 2.0 endpoint for Model Context Protocol (MCP) tool management and invocation.

## Installation

```bash
pip install -r requirements.txt
```

## Running the MCP Server

```bash
uvicorn mcp_server.main:create_app --factory --reload
```

The server will be running at http://127.0.0.1:8000/mcp

## Available JSON-RPC Methods

- `hello()`: Returns a greeting and server version.
- `list_tools()`: Lists registered tools with their names, descriptions, and argument schemas.
- `call_tool(name: str, args: dict)`: Calls a registered tool with arguments.

## Example JSON-RPC Request (curl)

```bash
curl -X POST http://127.0.0.1:8000/mcp \
  -H "Content-Type: application/json" \
  -d '{
        "jsonrpc":"2.0",
        "id":1,
        "method":"call_tool",
        "params": {
            "name": "add",
            "args": { "a": 2, "b": 3 }
        }
      }'
```

**Expected Response:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "result": 5
  }
}
```

---

## MetaGPT Client Usage

Run the client and pass the prompt as an argument:

```bash
python metagpt_client.py "Hello MetaGPT"
```

The script prints the response from the MetaGPT API.

