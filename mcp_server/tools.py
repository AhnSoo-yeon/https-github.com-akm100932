"""
tools.py

Defines demo tools for the MCP server.
"""

from typing import Callable, Any, Dict, List, Optional
from pydantic import BaseModel, Field

# Tool Registry
class Tool:
    def __init__(self, name: str, func: Callable, description: str, param_schema: type):
        self.name = name
        self.func = func
        self.description = description
        self.param_schema = param_schema

class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Tool] = {}

    def register(self, name: str, func: Callable, description: str, param_schema: type):
        self._tools[name] = Tool(name, func, description, param_schema)

    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)

    def list_tools(self) -> List[Tool]:
        return list(self._tools.values())

tool_registry = ToolRegistry()

# Tool param/result schemas
class EchoParams(BaseModel):
    text: str = Field(..., description="Text to echo.")

class EchoResult(BaseModel):
    result: str

class AddParams(BaseModel):
    a: int = Field(..., description="First integer.")
    b: int = Field(..., description="Second integer.")

class AddResult(BaseModel):
    result: int

# Tool implementations
async def echo(params: EchoParams) -> EchoResult:
    """Echoes back the input text."""
    return EchoResult(result=params.text)

async def add(params: AddParams) -> AddResult:
    """Returns the sum of two integers."""
    return AddResult(result=params.a + params.b)

# Register tools
tool_registry.register(
    name="echo",
    func=echo,
    description="Echo back the input text.",
    param_schema=EchoParams,
)
tool_registry.register(
    name="add",
    func=add,
    description="Add two integers.",
    param_schema=AddParams
)