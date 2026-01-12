import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator

class InteractionState(TypedDict):
    messages: Annotated[list, operator.add]
    current_step: str
    needs_approval: bool
    user_response: str
    final_result: str

def prepare_request(state: InteractionState) -> InteractionState:
    """Prepare a request that needs human approval."""
    return {
        "messages": ["System: Preparing data processing request..."],
        "current_step": "prepared",
        "needs_approval": True
    }

def wait_for_human(state: InteractionState) -> InteractionState:
    """Wait for human input."""
    return {
        "messages": ["System: Waiting for human approval..."],
        "current_step": "waiting"
    }

st.title("Example 04 Human in the Loop")
if st.button("Start", type="primary"):
    try:
        st.write(prepare_request({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
