import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
from datetime import datetime

class ChatState(TypedDict):
    messages: Annotated[list, operator.add]
    context: dict

def understand_intent(state: ChatState) -> ChatState:
    """Understand user intent from the last message."""
    user_messages = [m for m in state["messages"] if m["role"] == "user"]
    if not user_messages:
        return {"messages": [], "context": {}}
    
    last_msg = user_messages[-1]["content"].lower()
    
    # Intent classification
    if any(word in last_msg for word in ["hello", "hi", "hey"]):
        intent = "greeting"
    elif any(word in last_msg for word in ["bye", "goodbye", "see you"]):
        intent = "farewell"
    elif "?" in last_msg:
        intent = "question"
    elif any(word in last_msg for word in ["thank", "thanks"]):
        intent = "gratitude"
    else:
        intent = "statement"
    
    return {
        "context": {"intent": intent, "last_user_msg": user_messages[-1]["content"]}
    }

def generate_response(state: ChatState) -> ChatState:
    """Generate response based on intent."""
    intent = state["context"].get("intent", "unknown")
    last_msg = state["context"].get("last_user_msg", "")
    
    responses = {
        "greeting": "Hello! 👋 Great to chat with you! How can I assist you today?",
        "farewell": "Goodbye! 👋 Take care and have a wonderful day!",
        "question": f"That's an interesting question! You asked: '{last_msg}'. Let me think about that...",
        "gratitude": "You're very welcome! 😊 Happy to help!",
        "statement": f"I see! You mentioned: '{last_msg}'. Tell me more!",
        "unknown": "I'm here to chat! Feel free to ask me anything."
    }
    
    response = responses.get(intent, responses["unknown"])
    
    return {
        "messages": [{
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().strftime("%H:%M:%S"),
            "intent": intent
        }]
    }

def create_graph():
    workflow = StateGraph(ChatState)
    
    # Add nodes
    workflow.add_node("understand", understand_intent)
    workflow.add_node("respond", generate_response)
    
    # Add edges
    workflow.set_entry_point("understand")
    workflow.add_edge("understand", "respond")
    workflow.add_edge("respond", END)
    
    return workflow.compile()

st.title("Example 06 Simple Chatbot")
if st.button("Start", type="primary"):
    try:
        st.write(understand_intent({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
