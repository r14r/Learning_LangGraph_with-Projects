import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
from datetime import datetime

# Define the state structure
class ChatState(TypedDict):
    messages: Annotated[list, operator.add]
    context: dict

# Node functions
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

# Create the graph
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

# Streamlit UI
st.title("🤖 Simple Chatbot")
st.markdown("### Example 6: Intent-Based Chat System")

st.markdown("""
This chatbot demonstrates intent recognition and response generation:
- Classifies user intent (greeting, farewell, question, etc.)
- Generates appropriate responses
- Maintains conversation history
""")

# Initialize session state
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []
    # Add welcome message
    st.session_state.chat_messages.append({
        "role": "assistant",
        "content": "👋 Hello! I'm a simple chatbot. Try greeting me, asking questions, or just chat!",
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "intent": "greeting"
    })

# Display chat messages
st.markdown("### 💬 Conversation")
chat_container = st.container()
with chat_container:
    for msg in st.session_state.chat_messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div style='background-color: #e3f2fd; padding: 10px; border-radius: 10px; margin: 5px 0;'>
                <b>You</b> ({msg['timestamp']}): {msg['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            intent_emoji = {
                "greeting": "👋",
                "farewell": "👋",
                "question": "❓",
                "gratitude": "😊",
                "statement": "💭",
                "unknown": "🤖"
            }.get(msg.get("intent", "unknown"), "🤖")
            
            st.markdown(f"""
            <div style='background-color: #f5f5f5; padding: 10px; border-radius: 10px; margin: 5px 0;'>
                <b>Bot {intent_emoji}</b> ({msg['timestamp']}): {msg['content']}
            </div>
            """, unsafe_allow_html=True)

# Chat input
st.markdown("### ✍️ Your Message")
col1, col2 = st.columns([4, 1])

with col1:
    user_input = st.text_input("Type your message:", key="chat_input", label_visibility="collapsed")

with col2:
    send_button = st.button("Send", type="primary", use_container_width=True)

if send_button and user_input:
    # Add user message
    user_msg = {
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    }
    st.session_state.chat_messages.append(user_msg)
    
    # Generate response
    graph = create_graph()
    state = {
        "messages": st.session_state.chat_messages,
        "context": {}
    }
    result = graph.invoke(state)
    st.session_state.chat_messages = result["messages"]
    st.rerun()

# Action buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Clear Chat", use_container_width=True):
        st.session_state.chat_messages = []
        st.rerun()

with col2:
    if st.button("Say Hello", use_container_width=True):
        st.session_state.chat_messages.append({
            "role": "user",
            "content": "Hello!",
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        graph = create_graph()
        state = {"messages": st.session_state.chat_messages, "context": {}}
        result = graph.invoke(state)
        st.session_state.chat_messages = result["messages"]
        st.rerun()

with col3:
    if st.button("Ask Question", use_container_width=True):
        st.session_state.chat_messages.append({
            "role": "user",
            "content": "What can you do?",
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })
        graph = create_graph()
        state = {"messages": st.session_state.chat_messages, "context": {}}
        result = graph.invoke(state)
        st.session_state.chat_messages = result["messages"]
        st.rerun()

# Stats
st.markdown("### 📊 Chat Statistics")
user_count = len([m for m in st.session_state.chat_messages if m["role"] == "user"])
bot_count = len([m for m in st.session_state.chat_messages if m["role"] == "assistant"])
st.write(f"**Total Messages:** {len(st.session_state.chat_messages)} | **You:** {user_count} | **Bot:** {bot_count}")

# Display graph visualization
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → understand → respond → END
    ```
    
    **Processing Pipeline:**
    1. **understand**: Classifies user intent
       - Greeting (hello, hi, hey)
       - Farewell (bye, goodbye)
       - Question (contains ?)
       - Gratitude (thank, thanks)
       - Statement (default)
    
    2. **respond**: Generates contextual response based on intent
    """)

with st.expander("💡 Try These Examples"):
    st.markdown("""
    - **Greeting:** "Hello!", "Hi there"
    - **Question:** "What can you do?", "How are you?"
    - **Thanks:** "Thank you", "Thanks a lot"
    - **Farewell:** "Goodbye", "See you later"
    - **Statement:** "I like chatbots", "This is interesting"
    """)
