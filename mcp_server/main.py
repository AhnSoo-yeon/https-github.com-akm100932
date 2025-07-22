"""
main.py

Sets up the FastAPI app with JSON-RPC entrypoint and CORS.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mcp_server.endpoints import router

def create_app() -> FastAPI:
    """
    Creates and configures the FastAPI MCP server app.

    Returns:
        FastAPI: The FastAPI application.
    """
    app = FastAPI(title="Model Context Protocol (MCP) Server", version="0.1.0")

    # CORS (allow all for demo)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Mount JSON-RPC entrypoint
    app.include_router(router)
    return app