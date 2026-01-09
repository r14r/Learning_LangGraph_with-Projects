import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
from datetime import datetime

# Define the state structure
class ConversationState(TypedDict):
    messages: Annotated[list, operator.add]
    user_name: str
    conversation_start: str

# Node functions
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

# Create the graph
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

# Streamlit UI
st.title("💬 Message History")
st.markdown("### Example 5: Conversation with Memory")

st.markdown("""
This example demonstrates maintaining conversation history in LangGraph:
- Tracks all messages in the conversation
- Maintains context across interactions
- Shows timestamped message history
""")

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'conversation_started' not in st.session_state:
    st.session_state.conversation_started = False

# User name input
if not st.session_state.conversation_started:
    user_name = st.text_input("What's your name?", value="Guest")
    if st.button("Start Conversation", type="primary"):
        st.session_state.user_name = user_name
        st.session_state.conversation_started = True
        st.session_state.conversation_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Initialize with greeting
        graph = create_graph()
        initial_state = {
            "messages": [],
            "user_name": user_name,
            "conversation_start": st.session_state.conversation_start
        }
        result = graph.invoke(initial_state)
        st.session_state.conversation_history = result["messages"]
        st.rerun()
else:
    # Display conversation
    st.markdown(f"**Chatting as:** {st.session_state.user_name}")
    st.markdown(f"**Started:** {st.session_state.conversation_start}")
    
    # Message history display
    st.markdown("### 📜 Conversation History")
    with st.container():
        for msg in st.session_state.conversation_history:
            if msg["role"] == "user":
                st.markdown(f"**You** ({msg['timestamp']}): {msg['content']}")
            else:
                st.info(f"**{msg['content']}** ({msg['timestamp']})")
    
    # Input for new message
    st.markdown("### ✍️ Send a Message")
    user_input = st.text_input("Your message:", key="user_input")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Send", type="primary"):
            if user_input:
                # Add user message to history
                user_message = {
                    "role": "user",
                    "content": user_input,
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                }
                st.session_state.conversation_history.append(user_message)
                
                # Process response
                graph = create_graph()
                state = {
                    "messages": st.session_state.conversation_history,
                    "user_name": st.session_state.user_name,
                    "conversation_start": st.session_state.conversation_start
                }
                result = graph.invoke(state)
                st.session_state.conversation_history = result["messages"]
                st.rerun()
    
    with col2:
        if st.button("Clear History"):
            st.session_state.conversation_history = []
            st.session_state.conversation_started = False
            st.session_state.user_name = ""
            st.rerun()
    
    # Stats
    st.markdown("### 📊 Conversation Stats")
    user_msg_count = len([m for m in st.session_state.conversation_history if m["role"] == "user"])
    bot_msg_count = len([m for m in st.session_state.conversation_history if m["role"] == "assistant"])
    st.write(f"**Total Messages:** {len(st.session_state.conversation_history)}")
    st.write(f"**Your Messages:** {user_msg_count}")
    st.write(f"**Bot Messages:** {bot_msg_count}")

# Display graph visualization
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → greet → respond → END
    ```
    
    - **greet**: Initial greeting with user's name
    - **respond**: Processes user message and generates response
    
    **State Management:**
    - Messages are accumulated using `Annotated[list, operator.add]`
    - Each message includes role, content, and timestamp
    - Full history is maintained in session state
    """)
