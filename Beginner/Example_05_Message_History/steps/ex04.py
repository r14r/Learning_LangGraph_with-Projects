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

def process_message(state: ConversationState) -> ConversationState:
    """Process the user's message."""
    # Get the last user message
    user_messages = [m for m in state["messages"] if m["role"] == "user"]
    if user_messages:
        last_message = user_messages[-1]["content"].lower()
        
        # Simple response logic
        if "hello" in last_message or "hi" in last_message:
            response = "Bot: Hello! Nice to hear from you!"
        elif "how are you" in last_message:
            response = "Bot: I'm doing great! Thanks for asking. How about you?"
        elif "bye" in last_message or "goodbye" in last_message:
            response = "Bot: Goodbye! Have a great day!"
        elif "help" in last_message:
            response = "Bot: I can chat with you! Try saying hello, asking how I am, or saying goodbye."
        elif "weather" in last_message:
            response = "Bot: I don't have access to weather data, but I hope it's nice where you are!"
        else:
            response = f"Bot: I heard you say '{user_messages[-1]['content']}'. That's interesting!"
        
        return {
            "messages": [{"role": "assistant", "content": response, "timestamp": datetime.now().strftime("%H:%M:%S")}]
        }
    return {"messages": []}

def create_graph():
    workflow = StateGraph(ConversationState)
    
    # Add nodes
    workflow.add_node("greet", greet_user)
    workflow.add_node("respond", process_message)
    
    # Add edges
    workflow.set_entry_point("greet")
    workflow.add_edge("greet", "respond")
    workflow.add_edge("respond", END)
    
    return workflow.compile()

st.title("Example 05 Message History")
if st.button("Start", type="primary"):
    try:
        st.write(greet_user({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
