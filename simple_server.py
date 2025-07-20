from mcp.server.fastmcp import FastMCP
import math
from datetime import datetime
import os

# Set environment variables for port configuration
os.environ["MCP_PORT"] = "8090"

# Create an MCP server instance
mcp = FastMCP(
    "Simple MCP Server",
    dependencies=[]
)

# Define some basic tools

@mcp.tool()
def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The result of a - b
    """
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """
    Divide first number by second.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        The result of a / b
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def get_datetime() -> str:
    """
    Get current date and time.
    
    Returns:
        Current date and time as a formatted string
    """
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the server
if __name__ == "__main__":
    print("Starting MCP server on http://localhost:8090")
    mcp.run()
