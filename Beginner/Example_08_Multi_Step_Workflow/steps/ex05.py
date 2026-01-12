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

st.title("📋 Multi-Step Workflow")
st.markdown("### Example 8: Sequential Processing Pipeline")

st.markdown("Demonstrates a multi-step data processing workflow with 4 sequential steps.")

if st.button("Run Workflow", type="primary"):
    with st.spinner("Processing workflow..."):
        graph = create_graph()
        result = graph.invoke({"data": {}, "steps_completed": [], "status": "started"})
        st.success(f"Workflow completed with status: {result['status']}")
        for step in result["steps_completed"]:
            st.write(f"✅ {step}")

with st.expander("📊 Workflow Diagram"):
    st.markdown("```\nSTART → collect → validate → process → save → END\n```")
