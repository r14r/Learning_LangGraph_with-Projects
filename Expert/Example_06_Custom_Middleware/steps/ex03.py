import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

class ExampleState(TypedDict):
    input: str
    output: str
    steps: Annotated[list, operator.add]

def process_node(state: ExampleState) -> ExampleState:
    """Process the input."""
    return {
        "output": f"Processed: {state['input']}",
        "steps": ["Processing completed"]
    }

st.title("Example 06 Custom Middleware")
if st.button("Start", type="primary"):
    try:
        st.write(process_node({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
