import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

class WorkflowState(TypedDict):
    data: dict
    steps_completed: Annotated[list, operator.add]
    status: str

def step1_collect_data(state: WorkflowState) -> WorkflowState:
    return {"steps_completed": ["Step 1: Data collected"], "status": "collecting"}

def step2_validate_data(state: WorkflowState) -> WorkflowState:
    return {"steps_completed": ["Step 2: Data validated"], "status": "validating"}

st.title("Example 08 Multi Step Workflow")
if st.button("Start", type="primary"):
    try:
        st.write(step1_collect_data({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
