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

def parse_query(state: ToolState) -> ToolState:
    """Parse the query and determine which tool to use."""
    query = state["query"].lower()
    
    # Determine tool type
    if any(word in query for word in ["calculate", "add", "subtract", "multiply", "divide", "math"]):
        tool = "calculator"
    elif any(word in query for word in ["text", "string", "uppercase", "lowercase", "reverse"]):
        tool = "string"
    else:
        tool = "unknown"
    
    return {
        "tool_calls": [{"tool": tool, "query": query}]
    }

def execute_tool(state: ToolState) -> ToolState:
    """Execute the appropriate tool."""
    if not state["tool_calls"]:
        return {"result": "No tool selected"}
    
    last_call = state["tool_calls"][-1]
    tool = last_call["tool"]
    
    if tool == "calculator":
        result = "Calculator result: Use the calculator inputs below"
    elif tool == "string":
        result = "String tool result: Use the string tools below"
    else:
        result = "Unknown tool requested"
    
    return {"result": result}

def create_graph():
    workflow = StateGraph(ToolState)
    
    # Add nodes
    workflow.add_node("parse", parse_query)
    workflow.add_node("execute", execute_tool)
    
    # Add edges
    workflow.set_entry_point("parse")
    workflow.add_edge("parse", "execute")
    workflow.add_edge("execute", END)
    
    return workflow.compile()

st.title("Example 07 Tool Calling")
if st.button("Start", type="primary"):
    try:
        st.write(parse_query({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
