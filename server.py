from mcp.server.fastmcp import FastMCP
import math

# Initialize the MCP server with a title
mcp = FastMCP("Math Tool Server")

# TOOLS with metadata

@mcp.tool(description="Add two integers")
def add(a: int, b: int) -> int:
    return a + b


@mcp.tool(description="Subtract two integers")
def subtract(a: int, b: int) -> int:
    return a - b

# RUN MCP on HTTP port
if __name__ == "__main__":
    mcp.run()



