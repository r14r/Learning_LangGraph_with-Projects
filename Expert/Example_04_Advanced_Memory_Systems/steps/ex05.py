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

st.title("🎯 Advanced Memory Systems")
st.markdown(f"### Example 4: Sophisticated memory management")

st.markdown(f"""
This Expert level example demonstrates: **Sophisticated memory management**

This is a template example showing basic LangGraph structure.
""")

user_input = st.text_input("Enter your input:", value="test input")

if st.button("Process", type="primary"):
    with st.spinner("Processing..."):
        graph = create_graph()
        result = graph.invoke({"input": user_input, "output": "", "steps": []})
        
        st.success("Processing Complete!")
        st.write(f"**Output:** {result['output']}")
        st.write(f"**Steps:** {result['steps']}")

with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → process → END
    ```
    """)
