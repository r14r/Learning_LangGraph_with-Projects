import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
from datetime import datetime

class ConversationState(TypedDict):
    messages: Annotated[list, operator.add]
    user_name: str
    conversation_start: str

def greet_user(state: ConversationState) -> ConversationState:
    """Greet the user."""
    name = state.get("user_name", "User")
    greeting = f"Bot: Hello {name}! How can I help you today?"
    return {
        "messages": [{"role": "assistant", "content": greeting, "timestamp": datetime.now().strftime("%H:%M:%S")}]
    }

st.title("Example 05 Message History")
if st.button("Start", type="primary"):
    try:
        st.write(greet_user({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
