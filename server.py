"""
Root entrypoint for FLI MCP server.

For Prefect Horizon, use:
    server.py:mcp

For local HTTP testing, run:
    python server.py
"""

from fli.mcp.server import mcp, run_http


def main() -> None:
    """Run the MCP server locally over HTTP."""
    run_http()


if __name__ == "__main__":
    main()
