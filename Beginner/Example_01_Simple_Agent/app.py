import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

# Define the state structure
class AgentState(TypedDict):
    input: str
    output: str
    steps: Annotated[list, operator.add]

# Define node functions
def process_input(state: AgentState) -> AgentState:
    """Process the input and generate a response."""
    user_input = state["input"]
    response = f"Processed: {user_input.upper()}"
    return {
        "output": response,
        "steps": [f"Step 1: Received input '{user_input}'"]
    }

def finalize_output(state: AgentState) -> AgentState:
    """Finalize the output."""
    return {
        "output": state["output"] + " [FINAL]",
        "steps": ["Step 2: Finalized output"]
    }

# Create the graph
def create_graph():
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("process", process_input)
    workflow.add_node("finalize", finalize_output)
    
    # Add edges
    workflow.set_entry_point("process")
    workflow.add_edge("process", "finalize")
    workflow.add_edge("finalize", END)
    
    return workflow.compile()

# Streamlit UI
st.title("🤖 Simple LangGraph Agent")
st.markdown("### Example 1: Basic Agent with Sequential Processing")

st.markdown("""
This example demonstrates a simple LangGraph agent with two sequential steps:
1. **Process Input**: Transforms the input text
2. **Finalize Output**: Adds a final marker to the output
""")

# Input section
user_input = st.text_input("Enter your text:", value="Hello LangGraph")

if st.button("Process", type="primary"):
    if user_input:
        with st.spinner("Processing..."):
            # Create and run the graph
            graph = create_graph()
            initial_state = {
                "input": user_input,
                "output": "",
                "steps": []
            }
            
            result = graph.invoke(initial_state)
            
            # Display results
            st.success("Processing Complete!")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Input:**")
                st.info(user_input)
            
            with col2:
                st.markdown("**Output:**")
                st.success(result["output"])
            
            st.markdown("**Processing Steps:**")
            for step in result["steps"]:
                st.write(f"✅ {step}")
    else:
        st.warning("Please enter some text to process.")

# Display graph visualization info
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → process → finalize → END
    ```
    
    - **process**: Transforms input to uppercase
    - **finalize**: Adds [FINAL] marker
    """)
