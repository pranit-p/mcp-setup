# Simple MCP Server

This is a simple Model Context Protocol (MCP) server that provides various tools via HTTP protocol for LLM integration.

## Setup

1. Install the required dependencies:

```bash
pip install mcp-server requests
```

2. Run the MCP server:

```bash
python enhanced_server.py
```

This will start the MCP server on `http://localhost:8080`.

## Available Tools

The MCP server provides the following tools:

### Math Operations

- `add`: Add two numbers
- `subtract`: Subtract second number from first
- `multiply`: Multiply two numbers
- `divide`: Divide first number by second

### Utility Tools

- `get_datetime`: Get current date and time
- `fetch_url`: Fetch data from a URL
- `convert_units`: Convert between common units (length and temperature)

## Testing the Server

You can test the server using the provided client script:

```bash
python mcp_client.py
```

## Connecting with Amazon Q

To connect this MCP server with Amazon Q:

1. Make sure the MCP server is running
2. Use the Amazon Q CLI with the `--mcp-server` flag:

```bash
q chat --mcp-server http://localhost:8080
```

3. In your chat with Amazon Q, you can now use the tools provided by your MCP server by referring to them with the server name prefix.

## Example Prompts for Amazon Q

Once connected, you can ask Amazon Q to use your MCP tools:

- "Calculate 25 + 17 using the MCP server's add tool"
- "What's the current date and time according to the MCP server?"
- "Convert 100 cm to inches using the MCP server"
- "Fetch data from https://jsonplaceholder.typicode.com/todos/1 using the MCP server"

## Extending the Server

To add more tools to the server, edit the `enhanced_server.py` file and add new functions with the `@mcp.tool` decorator. Each function should have:

- A descriptive name
- Type hints for parameters and return value
- A docstring describing what the tool does

Example:

```python
@mcp.tool(description="Calculate the square root of a number")
def square_root(number: float) -> float:
    """Calculate the square root of the given number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)
```
