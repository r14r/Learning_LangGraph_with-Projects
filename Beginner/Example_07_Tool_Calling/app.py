import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator
import math

# Define the state structure
class ToolState(TypedDict):
    query: str
    tool_calls: Annotated[list, operator.add]
    result: str

# Tool functions
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

# Node functions
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

# Create the graph
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

# Streamlit UI
st.title("🛠️ Tool Calling")
st.markdown("### Example 7: Using Tools in LangGraph")

st.markdown("""
This example demonstrates tool calling in LangGraph:
- **Calculator Tool**: Performs mathematical operations
- **String Tool**: Manipulates text
- Query parsing and tool selection
""")

# Tool selector
st.markdown("### 🎯 Select a Tool")
tool_type = st.radio("Choose tool type:", ["Calculator", "String Tools"], horizontal=True)

if tool_type == "Calculator":
    st.markdown("#### 🔢 Calculator Tool")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("First number:", value=10.0)
    with col2:
        operation = st.selectbox("Operation:", ["add", "subtract", "multiply", "divide", "power", "sqrt"])
    with col3:
        num2 = st.number_input("Second number:", value=5.0)
    
    if st.button("Calculate", type="primary"):
        with st.spinner("Calculating..."):
            # Create and run graph
            graph = create_graph()
            state = {
                "query": f"calculate {operation}",
                "tool_calls": [],
                "result": ""
            }
            result = graph.invoke(state)
            
            # Execute calculator
            calc_result = calculator(operation, num1, num2)
            
            st.success("Calculation Complete!")
            st.markdown(f"**Result:** `{num1} {operation} {num2} = {calc_result}`")
            
            st.markdown("**Tool Calls:**")
            for call in result["tool_calls"]:
                st.write(f"• Tool: {call['tool']}, Query: {call['query']}")

else:
    st.markdown("#### 📝 String Tools")
    
    text_input = st.text_input("Enter text:", value="Hello LangGraph")
    string_operation = st.selectbox("Operation:", ["uppercase", "lowercase", "reverse", "length", "capitalize"])
    
    if st.button("Process Text", type="primary"):
        with st.spinner("Processing..."):
            # Create and run graph
            graph = create_graph()
            state = {
                "query": f"string {string_operation}",
                "tool_calls": [],
                "result": ""
            }
            result = graph.invoke(state)
            
            # Execute string tool
            string_result = string_tool(string_operation, text_input)
            
            st.success("Processing Complete!")
            st.markdown(f"**Input:** {text_input}")
            st.markdown(f"**Result:** {string_result}")
            
            st.markdown("**Tool Calls:**")
            for call in result["tool_calls"]:
                st.write(f"• Tool: {call['tool']}, Query: {call['query']}")

# Display available tools
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → parse → execute → END
    ```
    
    **Processing Pipeline:**
    1. **parse**: Analyzes query and selects appropriate tool
    2. **execute**: Calls the selected tool with parameters
    
    **Available Tools:**
    - **Calculator**: add, subtract, multiply, divide, power, sqrt
    - **String**: uppercase, lowercase, reverse, length, capitalize
    """)

with st.expander("💡 Example Queries"):
    st.markdown("""
    **Calculator Examples:**
    - Add: 10 + 5 = 15
    - Multiply: 10 * 5 = 50
    - Power: 2 ** 3 = 8
    
    **String Examples:**
    - Uppercase: "hello" → "HELLO"
    - Reverse: "hello" → "olleh"
    - Length: "hello" → "Length: 5"
    """)
