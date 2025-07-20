import requests
import json

def call_mcp_tool(server_url, tool_name, params):
    """
    Call a tool on the MCP server
    
    Args:
        server_url (str): The URL of the MCP server
        tool_name (str): The name of the tool to call
        params (dict): The parameters to pass to the tool
        
    Returns:
        dict: The response from the MCP server
    """
    endpoint = f"{server_url}/tools/{tool_name}"
    
    try:
        response = requests.post(
            endpoint,
            json=params,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_available_tools(server_url):
    """
    Get a list of available tools from the MCP server
    
    Args:
        server_url (str): The URL of the MCP server
        
    Returns:
        dict: The response from the MCP server
    """
    try:
        response = requests.get(f"{server_url}/tools")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # MCP server URL
    server_url = "http://localhost:8080"
    
    # Get available tools
    print("Getting available tools...")
    tools = get_available_tools(server_url)
    print(json.dumps(tools, indent=2))
    
    # Example: Call the add tool
    print("\nCalling add tool...")
    add_result = call_mcp_tool(server_url, "add", {"a": 5, "b": 3})
    print(f"5 + 3 = {add_result}")
    
    # Example: Call the get_datetime tool
    print("\nCalling get_datetime tool...")
    datetime_result = call_mcp_tool(server_url, "get_datetime", {})
    print(f"Current date and time: {datetime_result}")
    
    # Example: Call the convert_units tool
    print("\nCalling convert_units tool...")
    conversion_result = call_mcp_tool(
        server_url, 
        "convert_units", 
        {"value": 100, "from_unit": "cm", "to_unit": "in"}
    )
    print(f"Conversion result: {conversion_result}")
