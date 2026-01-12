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

st.title("Example 01 Simple Agent")
if st.button("Start", type="primary"):
    try:
        st.write(process_input({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
