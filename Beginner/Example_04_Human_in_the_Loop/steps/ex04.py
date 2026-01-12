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

def process_approval(state: InteractionState) -> InteractionState:
    """Process after approval."""
    return {
        "messages": ["System: Processing approved request..."],
        "current_step": "approved",
        "final_result": "✅ Request approved and processed successfully!"
    }

def process_rejection(state: InteractionState) -> InteractionState:
    """Process after rejection."""
    return {
        "messages": ["System: Request was rejected by user."],
        "current_step": "rejected",
        "final_result": "❌ Request rejected by user."
    }

def check_approval(state: InteractionState) -> Literal["approved", "rejected"]:
    """Route based on user response."""
    return "approved" if state.get("user_response") == "approve" else "rejected"

st.title("Example 04 Human in the Loop")
if st.button("Start", type="primary"):
    try:
        st.write(prepare_request({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
