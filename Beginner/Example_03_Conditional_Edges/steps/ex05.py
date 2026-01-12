import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator

class ClassificationState(TypedDict):
    number: int
    classification: str
    route: str
    operations: Annotated[list, operator.add]
    result: str

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

def route_number(state: ClassificationState) -> Literal["positive", "negative", "zero"]:
    """Route based on classification."""
    return state["classification"]

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

st.title("Example 03 Conditional Edges")
if st.button("Start", type="primary"):
    try:
        st.write(classify_number({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
