"""
Prefect Horizon entrypoint for FLI MCP.

Horizon entrypoint:
    server.py:mcp
"""

import os

from fli.mcp.server import mcp


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
    )
