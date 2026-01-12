import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator
import math

class ToolState(TypedDict):
    query: str
    tool_calls: Annotated[list, operator.add]
    result: str

def calculator(operation: str, a: float, b: float) -> float:
    """Simple calculator tool."""
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y if y != 0 else "Error: Division by zero",
        "power": lambda x, y: x ** y,
        "sqrt": lambda x, y: math.sqrt(x)
    }
    return operations.get(operation, lambda x, y: "Unknown operation")(a, b)

def string_tool(operation: str, text: str) -> str:
    """String manipulation tool."""
    operations = {
        "uppercase": lambda t: t.upper(),
        "lowercase": lambda t: t.lower(),
        "reverse": lambda t: t[::-1],
        "length": lambda t: f"Length: {len(t)}",
        "capitalize": lambda t: t.capitalize()
    }
    return operations.get(operation, lambda t: t)(text)

st.title("Example 07 Tool Calling")
st.write("Step 3: Kernbausteine geladen.")
