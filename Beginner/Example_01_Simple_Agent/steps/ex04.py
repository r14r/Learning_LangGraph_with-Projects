import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

class AgentState(TypedDict):
    input: str
    output: str
    steps: Annotated[list, operator.add]

def process_input(state: AgentState) -> AgentState:
    """Process the input and generate a response."""
    user_input = state["input"]
    response = f"Processed: {user_input.upper()}"
    return {
        "output": response,
        "steps": [f"Step 1: Received input '{user_input}'"]
    }

def finalize_output(state: AgentState) -> AgentState:
    """Finalize the output."""
    return {
        "output": state["output"] + " [FINAL]",
        "steps": ["Step 2: Finalized output"]
    }

def create_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("process", process_input)
    workflow.add_node("finalize", finalize_output)
    
    # Add edges
    workflow.set_entry_point("process")
    workflow.add_edge("process", "finalize")
    workflow.add_edge("finalize", END)
    
    return workflow.compile()

st.title("Example 01 Simple Agent")
if st.button("Start", type="primary"):
    try:
        st.write(process_input({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
