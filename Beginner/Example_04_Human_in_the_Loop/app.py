import streamlit as st
from typing import TypedDict, Annotated, Literal
from langgraph.graph import StateGraph, END
import operator

# Define the state structure
class InteractionState(TypedDict):
    messages: Annotated[list, operator.add]
    current_step: str
    needs_approval: bool
    user_response: str
    final_result: str

# Node functions
def prepare_request(state: InteractionState) -> InteractionState:
    """Prepare a request that needs human approval."""
    return {
        "messages": ["System: Preparing data processing request..."],
        "current_step": "prepared",
        "needs_approval": True
    }

def wait_for_human(state: InteractionState) -> InteractionState:
    """Wait for human input."""
    return {
        "messages": ["System: Waiting for human approval..."],
        "current_step": "waiting"
    }

def process_approval(state: InteractionState) -> InteractionState:
    """Process after approval."""
    return {
        "messages": ["System: Processing approved request..."],
        "current_step": "approved",
        "final_result": "✅ Request approved and processed successfully!"
    }

def process_rejection(state: InteractionState) -> InteractionState:
    """Process after rejection."""
    return {
        "messages": ["System: Request was rejected by user."],
        "current_step": "rejected",
        "final_result": "❌ Request rejected by user."
    }

# Routing function
def check_approval(state: InteractionState) -> Literal["approved", "rejected"]:
    """Route based on user response."""
    return "approved" if state.get("user_response") == "approve" else "rejected"

# Create the graph
def create_graph():
    workflow = StateGraph(InteractionState)
    
    # Add nodes
    workflow.add_node("prepare", prepare_request)
    workflow.add_node("wait", wait_for_human)
    workflow.add_node("approve", process_approval)
    workflow.add_node("reject", process_rejection)
    
    # Set entry point
    workflow.set_entry_point("prepare")
    
    # Add edges
    workflow.add_edge("prepare", "wait")
    
    # Conditional edges based on human input
    workflow.add_conditional_edges(
        "wait",
        check_approval,
        {
            "approved": "approve",
            "rejected": "reject"
        }
    )
    
    workflow.add_edge("approve", END)
    workflow.add_edge("reject", END)
    
    return workflow.compile()

# Streamlit UI
st.title("👤 Human-in-the-Loop")
st.markdown("### Example 4: Interactive Approval Workflow")

st.markdown("""
This example demonstrates human-in-the-loop workflow in LangGraph:
1. **Prepare**: System prepares a request
2. **Wait**: Pauses for human decision
3. **Route**: Processes based on approval or rejection
""")

# Session state for tracking
if 'workflow_state' not in st.session_state:
    st.session_state.workflow_state = None
if 'workflow_started' not in st.session_state:
    st.session_state.workflow_started = False

# Start workflow
col1, col2 = st.columns(2)
with col1:
    if st.button("🚀 Start New Workflow", type="primary", disabled=st.session_state.workflow_started):
        st.session_state.workflow_started = True
        st.session_state.workflow_state = {
            "messages": [],
            "current_step": "initial",
            "needs_approval": False,
            "user_response": "",
            "final_result": ""
        }
        st.rerun()

with col2:
    if st.button("🔄 Reset"):
        st.session_state.workflow_started = False
        st.session_state.workflow_state = None
        st.rerun()

# Display workflow status
if st.session_state.workflow_started and st.session_state.workflow_state:
    st.info("**Status:** Workflow is active and waiting for your decision")
    
    st.markdown("### 📋 Request Details")
    st.write("""
    **Operation:** Data Processing Request
    **Description:** Process sensitive user data batch
    **Impact:** High
    **Estimated Time:** 5 minutes
    """)
    
    st.markdown("### ⚖️ Make Your Decision")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Approve", type="primary", use_container_width=True):
            # Process approval
            st.session_state.workflow_state["user_response"] = "approve"
            graph = create_graph()
            result = graph.invoke(st.session_state.workflow_state)
            st.session_state.workflow_state = result
            st.session_state.workflow_started = False
            st.rerun()
    
    with col2:
        if st.button("❌ Reject", type="secondary", use_container_width=True):
            # Process rejection
            st.session_state.workflow_state["user_response"] = "reject"
            graph = create_graph()
            result = graph.invoke(st.session_state.workflow_state)
            st.session_state.workflow_state = result
            st.session_state.workflow_started = False
            st.rerun()

# Display results if workflow completed
if st.session_state.workflow_state and not st.session_state.workflow_started:
    if st.session_state.workflow_state.get("final_result"):
        st.markdown("### 🎯 Result")
        if "approved" in st.session_state.workflow_state.get("current_step", ""):
            st.success(st.session_state.workflow_state["final_result"])
        else:
            st.error(st.session_state.workflow_state["final_result"])
        
        st.markdown("### 📝 Processing Log")
        for msg in st.session_state.workflow_state["messages"]:
            st.write(f"• {msg}")

# Display graph visualization
with st.expander("📊 Graph Structure"):
    st.markdown("""
    ```
    START → prepare → wait → [human decision]
                            ├→ approve → END
                            └→ reject → END
    ```
    
    **Human Decision Point:**
    - Workflow pauses at "wait" node
    - Requires user interaction (Approve/Reject)
    - Routes to appropriate handler
    """)

with st.expander("💡 Use Cases"):
    st.markdown("""
    - **Approval Workflows**: Require manager approval for operations
    - **Content Moderation**: Human review of AI-generated content
    - **Decision Support**: AI suggests, human decides
    - **Quality Control**: Manual verification of automated processes
    - **Compliance**: Human oversight for regulatory requirements
    """)
