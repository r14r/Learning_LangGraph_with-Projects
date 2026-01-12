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

def create_graph():
    workflow = StateGraph(ExampleState)
    workflow.add_node("process", process_node)
    workflow.set_entry_point("process")
    workflow.add_edge("process", END)
    return workflow.compile()

st.title("Example 09 Multi Modal Agents")
if st.button("Start", type="primary"):
    try:
        st.write(process_node({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
