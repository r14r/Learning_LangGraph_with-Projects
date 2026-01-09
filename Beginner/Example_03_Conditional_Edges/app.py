import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator

# Define the state structure
class ClassificationState(TypedDict):
    number: int
    classification: str
    route: str
    operations: Annotated[list, operator.add]
    result: str

# Node functions
def classify_number(state: ClassificationState) -> ClassificationState:
    """Classify the number as positive, negative, or zero."""
    num = state["number"]
    if num > 0:
        classification = "positive"
    elif num < 0:
        classification = "negative"
    else:
        classification = "zero"
    
    return {
        "classification": classification,
        "operations": [f"Classified {num} as {classification}"]
    }

def handle_positive(state: ClassificationState) -> ClassificationState:
    """Handle positive numbers."""
    result = f"✅ {state['number']} is positive! It's greater than zero."
    return {
        "result": result,
        "route": "positive",
        "operations": ["Processed through positive handler"]
    }

def handle_negative(state: ClassificationState) -> ClassificationState:
    """Handle negative numbers."""
    result = f"⚠️ {state['number']} is negative! It's less than zero."
    return {
        "result": result,
        "route": "negative",
        "operations": ["Processed through negative handler"]
    }

def handle_zero(state: ClassificationState) -> ClassificationState:
    """Handle zero."""
    result = f"⭕ {state['number']} is zero! It's neither positive nor negative."
    return {
        "result": result,
        "route": "zero",
        "operations": ["Processed through zero handler"]
    }

# Routing function
def route_number(state: ClassificationState) -> Literal["positive", "negative", "zero"]:
    """Route based on classification."""
    return state["classification"]

# Create the graph
def create_graph():
    workflow = StateGraph(ClassificationState)
    
    # Add nodes
    workflow.add_node("classify", classify_number)
    workflow.add_node("positive", handle_positive)
    workflow.add_node("negative", handle_negative)
    workflow.add_node("zero", handle_zero)
    
    # Set entry point
    workflow.set_entry_point("classify")
    
    # Add conditional edges
    workflow.add_conditional_edges(
        "classify",
        route_number,
        {
            "positive": "positive",
            "negative": "negative",
            "zero": "zero"
        }
    )
    
    # Add edges to END
    workflow.add_edge("positive", END)
    workflow.add_edge("negative", END)
    workflow.add_edge("zero", END)
    
    return workflow.compile()

# Streamlit UI
st.title("🔀 Conditional Edges")
st.markdown("### Example 3: Routing Based on Conditions")

st.markdown("""
This example demonstrates conditional routing in LangGraph:
1. **Classify**: Determines if the number is positive, negative, or zero
2. **Route**: Directs to the appropriate handler based on classification
3. **Handle**: Processes the number according to its type
""")

# Input section
col1, col2 = st.columns([2, 1])
with col1:
    number = st.number_input("Enter a number:", value=0, min_value=-100, max_value=100)
with col2:
    st.markdown("**Classification:**")
    if number > 0:
        st.success("Positive ✅")
    elif number < 0:
        st.warning("Negative ⚠️")
    else:
        st.info("Zero ⭕")

if st.button("Classify and Process", type="primary"):
    with st.spinner("Processing..."):
        # Create and run the graph
        graph = create_graph()
        initial_state = {
            "number": number,
            "classification": "",
            "route": "",
            "operations": [],
            "result": ""
        }
        
        result = graph.invoke(initial_state)
        
        # Display results
        st.success("Processing Complete!")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Input:**")
            st.info(number)
        
        with col2:
            st.markdown("**Classification:**")
            st.info(result["classification"].upper())
        
        with col3:
            st.markdown("**Route Taken:**")
            st.info(result["route"].upper())
        
        st.markdown("**Result:**")
        st.write(result["result"])
        
        st.markdown("**Processing Steps:**")
        for idx, operation in enumerate(result["operations"], 1):
            st.write(f"{idx}. {operation}")

# Display graph visualization
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → classify → [conditional routing]
                     ├→ positive → END
                     ├→ negative → END
                     └→ zero → END
    ```
    
    **Routing Logic:**
    - If number > 0 → positive handler
    - If number < 0 → negative handler
    - If number = 0 → zero handler
    """)

# Interactive examples
with st.expander("🎯 Try These Examples"):
    st.markdown("""
    | Number | Classification | Route | Description |
    |--------|---------------|-------|-------------|
    | 42     | Positive      | positive | Large positive number |
    | 1      | Positive      | positive | Small positive number |
    | 0      | Zero          | zero | Exactly zero |
    | -1     | Negative      | negative | Small negative number |
    | -42    | Negative      | negative | Large negative number |
    """)
