"""
endpoints.py

Defines the FastAPI JSON-RPC entrypoint and core MCP RPC methods.
"""

from typing import Any, Dict, List
from fastapi_jsonrpc import Entrypoint, JsonRpcRouter, BaseError
from pydantic import BaseModel, Field
from mcp_server.tools import tool_registry, Tool
import pkg_resources

SERVER_VERSION = "0.1.0"

class HelloResult(BaseModel):
    """Response for hello()"""
    greeting: str
    version: str

class ToolInfo(BaseModel):
    """Info about a registered tool."""
    name: str
    description: str
    params_schema: Dict[str, Any]

class CallToolParams(BaseModel):
    name: str = Field(..., description="Tool name to invoke.")
    args: Dict[str, Any] = Field(..., description="Arguments for the tool.")

class CallToolResult(BaseModel):
    result: Any

class ToolNotFoundError(BaseError):
    CODE = 404
    MESSAGE = "Tool not found"

# Entrypoint definition
router = Entrypoint("/mcp", tags=["mcp"])

@router.method()
async def hello() -> HelloResult:
    """
    Returns a greeting and MCP server version.

    Returns:
        HelloResult: The greeting and version info.
    """
    return HelloResult(greeting="Welcome to Model Context Protocol (MCP) server!", version=SERVER_VERSION)

@router.method()
async def list_tools() -> List[ToolInfo]:
    """
    Lists all available tools with name, description, and params schema.

    Returns:
        List[ToolInfo]: Tool info objects.
    """
    tools = []
    for tool in tool_registry.list_tools():
        schema = tool.param_schema.schema() if hasattr(tool.param_schema, "schema") else {}
        tools.append(
            ToolInfo(
                name=tool.name,
                description=tool.description,
                params_schema=schema.get("properties", {})
            )
        )
    return tools

@router.method()
async def call_tool(params: CallToolParams) -> CallToolResult:
    """
    Executes a named tool with arguments.

    Args:
        params (CallToolParams): Tool name and arguments.

    Returns:
        CallToolResult: Result of the tool invocation.

    Raises:
        ToolNotFoundError: If tool name is unknown.
    """
    tool = tool_registry.get(params.name)
    if not tool:
        raise ToolNotFoundError(data={"tool": params.name})
    # Validate args with param_schema
    validated = tool.param_schema(**params.args)
    result = await tool.func(validated)
    return CallToolResult(result=result.result if hasattr(result, "result") else result)