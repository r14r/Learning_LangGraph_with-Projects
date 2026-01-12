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

def step3_process_data(state: WorkflowState) -> WorkflowState:
    return {"steps_completed": ["Step 3: Data processed"], "status": "processing"}

def step4_save_results(state: WorkflowState) -> WorkflowState:
    return {"steps_completed": ["Step 4: Results saved"], "status": "completed"}

def create_graph():
    workflow = StateGraph(WorkflowState)
    workflow.add_node("collect", step1_collect_data)
    workflow.add_node("validate", step2_validate_data)
    workflow.add_node("process", step3_process_data)
    workflow.add_node("save", step4_save_results)
    workflow.set_entry_point("collect")
    workflow.add_edge("collect", "validate")
    workflow.add_edge("validate", "process")
    workflow.add_edge("process", "save")
    workflow.add_edge("save", END)
    return workflow.compile()

st.title("Example 08 Multi Step Workflow")
if st.button("Start", type="primary"):
    try:
        st.write(step1_collect_data({"input": "demo", "output": "", "steps": []}))
    except Exception as exc:
        st.error(str(exc))
