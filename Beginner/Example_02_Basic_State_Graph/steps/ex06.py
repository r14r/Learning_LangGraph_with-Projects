import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

# Define the state structure
class MathState(TypedDict):
    number: int
    operations: Annotated[list, operator.add]
    result: int

# Node functions
def add_ten(state: MathState) -> MathState:
    """Add 10 to the number."""
    new_result = state["number"] + 10
    return {
        "result": new_result,
        "operations": [f"Added 10: {state['number']} + 10 = {new_result}"]
    }

def multiply_by_two(state: MathState) -> MathState:
    """Multiply the result by 2."""
    new_result = state["result"] * 2
    return {
        "result": new_result,
        "operations": [f"Multiplied by 2: {state['result']} * 2 = {new_result}"]
    }

def subtract_five(state: MathState) -> MathState:
    """Subtract 5 from the result."""
    new_result = state["result"] - 5
    return {
        "result": new_result,
        "operations": [f"Subtracted 5: {state['result']} - 5 = {new_result}"]
    }

# Create the graph
def create_graph():
    workflow = StateGraph(MathState)
    
    # Add nodes
    workflow.add_node("add", add_ten)
    workflow.add_node("multiply", multiply_by_two)
    workflow.add_node("subtract", subtract_five)
    
    # Add edges
    workflow.set_entry_point("add")
    workflow.add_edge("add", "multiply")
    workflow.add_edge("multiply", "subtract")
    workflow.add_edge("subtract", END)
    
    return workflow.compile()

# Streamlit UI
st.title("🔢 Basic State Graph")
st.markdown("### Example 2: Sequential Mathematical Operations")

st.markdown("""
This example demonstrates state management in LangGraph through a series of mathematical operations:
1. **Add 10**: Adds 10 to the input number
2. **Multiply by 2**: Multiplies the result by 2
3. **Subtract 5**: Subtracts 5 from the result

Formula: `((number + 10) * 2) - 5`
""")

# Input section
col1, col2 = st.columns([2, 1])
with col1:
    number = st.number_input("Enter a number:", value=5, min_value=-1000, max_value=1000)
with col2:
    st.markdown("**Quick Test:**")
    st.info(f"Expected: {((number + 10) * 2) - 5}")

if st.button("Calculate", type="primary"):
    with st.spinner("Processing..."):
        # Create and run the graph
        graph = create_graph()
        initial_state = {
            "number": number,
            "operations": [],
            "result": number
        }
        
        result = graph.invoke(initial_state)
        
        # Display results
        st.success("Calculation Complete!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Initial Number:**")
            st.info(number)
        
        with col2:
            st.markdown("**Final Result:**")
            st.success(result["result"])
        
        st.markdown("**Operations Performed:**")
        for idx, operation in enumerate(result["operations"], 1):
            st.write(f"{idx}. {operation}")
        
        # Verification
        expected = ((number + 10) * 2) - 5
        if result["result"] == expected:
            st.success(f"✅ Verification passed! Result matches expected value: {expected}")
        else:
            st.error(f"❌ Verification failed! Expected {expected} but got {result['result']}")

# Display graph visualization
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → add (+10) → multiply (*2) → subtract (-5) → END
    ```
    
    - **add**: number + 10
    - **multiply**: result * 2  
    - **subtract**: result - 5
    """)

# Example calculations
with st.expander("📝 Example Calculations"):
    st.markdown("""
    | Input | After Add | After Multiply | After Subtract |
    |-------|-----------|----------------|----------------|
    | 5     | 15        | 30             | 25             |
    | 0     | 10        | 20             | 15             |
    | -3    | 7         | 14             | 9              |
    | 10    | 20        | 40             | 35             |
    """)
