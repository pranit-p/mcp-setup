from mcp.server.fastmcp import FastMCP
import math
import datetime
import requests
import json
from typing import Dict, List, Optional, Any

# Initialize the MCP server with a title

# mcp = FastMCP("strava", stateless_http=True, host="127.0.0.1", port=8000)
mcp = FastMCP("strava", stateless_http=True)


# Math Tools
@mcp.tool(description="Add two numbers")
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool(description="Subtract second number from first")
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@mcp.tool(description="Multiply two numbers")
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@mcp.tool(description="Divide first number by second")
def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Utility Tools
@mcp.tool(description="Get current date and time")
def get_datetime() -> Dict[str, str]:
    """Return the current date and time."""
    now = datetime.datetime.now()
    return {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "day_of_week": now.strftime("%A"),
        "timestamp": now.isoformat()
    }

@mcp.tool(description="Fetch data from a URL")
def fetch_url(url: str) -> Dict[str, Any]:
    """Fetch data from a URL and return the response."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Try to parse as JSON first
        try:
            return {
                "status_code": response.status_code,
                "content_type": response.headers.get("Content-Type", ""),
                "data": response.json(),
                "is_json": True
            }
        except json.JSONDecodeError:
            # If not JSON, return as text
            return {
                "status_code": response.status_code,
                "content_type": response.headers.get("Content-Type", ""),
                "data": response.text[:1000],  # Limit text size
                "is_json": False
            }
    except Exception as e:
        return {"error": str(e)}

@mcp.tool(description="Convert between units")
def convert_units(value: float, from_unit: str, to_unit: str) -> Dict[str, Any]:
    """
    Convert between common units.
    Supported unit types: length (m, km, cm, mm, ft, in), temperature (C, F, K)
    """
    # Length conversions to meters (base unit)
    length_to_m = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "ft": 0.3048,
        "in": 0.0254
    }
    
    # Temperature conversions
    if from_unit in ["C", "F", "K"] and to_unit in ["C", "F", "K"]:
        # Convert to Kelvin first (base unit)
        if from_unit == "C":
            kelvin = value + 273.15
        elif from_unit == "F":
            kelvin = (value - 32) * 5/9 + 273.15
        else:  # K
            kelvin = value
            
        # Convert from Kelvin to target
        if to_unit == "C":
            result = kelvin - 273.15
        elif to_unit == "F":
            result = (kelvin - 273.15) * 9/5 + 32
        else:  # K
            result = kelvin
            
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": result,
            "converted_unit": to_unit,
            "conversion_type": "temperature"
        }
    
    # Length conversions
    elif from_unit in length_to_m and to_unit in length_to_m:
        # Convert to meters first, then to target unit
        meters = value * length_to_m[from_unit]
        result = meters / length_to_m[to_unit]
        
        return {
            "original_value": value,
            "original_unit": from_unit,
            "converted_value": result,
            "converted_unit": to_unit,
            "conversion_type": "length"
        }
    else:
        return {"error": f"Unsupported unit conversion from {from_unit} to {to_unit}"}

# Run the MCP server on HTTP port 8080


@mcp.tool()
def hello_world() -> str:
    """Return the text 'hello world!'."""
    return "hello world!"


if __name__ == "__main__":
    print("Hello")
    mcp.run(transport='streamable-http')



# if __name__ == "__main__":
#     # FastMCP.run() doesn't accept host and port directly
#     mcp.run(transport='streamable-http')
