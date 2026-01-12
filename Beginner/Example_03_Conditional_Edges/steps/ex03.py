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

st.title("Example 03 Conditional Edges")
if st.button("Start", type="primary"):
    try:
        st.write(classify_number({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
