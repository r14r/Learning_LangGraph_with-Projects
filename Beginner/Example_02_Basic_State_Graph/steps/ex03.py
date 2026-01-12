import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

class MathState(TypedDict):
    number: int
    operations: Annotated[list, operator.add]
    result: int

def add_ten(state: MathState) -> MathState:
    """Add 10 to the number."""
    new_result = state["number"] + 10
    return {
        "result": new_result,
        "operations": [f"Added 10: {state['number']} + 10 = {new_result}"]
    }

st.title("Example 02 Basic State Graph")
if st.button("Start", type="primary"):
    try:
        st.write(add_ten({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
