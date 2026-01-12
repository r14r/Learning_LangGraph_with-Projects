# Example 04: Human-in-the-Loop

## Overview
Demonstrates human-in-the-loop workflow where execution pauses for human decision-making.

## What to Do
This example creates an interactive workflow that:
1. Prepares a request requiring approval
2. Pauses execution and waits for human input
3. Routes based on user decision (approve/reject)
4. Completes processing based on the decision

## Inputs
- **User Decision**: Binary choice made during workflow execution
  - Type: String literal ("approve" or "reject")
  - Trigger: Button click in UI
  - Examples: "approve", "reject"

## Expected Outputs
- **Final Result**: Message indicating workflow outcome
  - Approved: "✅ Request approved and processed successfully!"
  - Rejected: "❌ Request rejected by user."

- **Messages**: Log of workflow steps
  - Preparation message
  - Waiting message
  - Processing message

- **Current Step**: State of workflow
  - Values: "initial", "prepared", "waiting", "approved", "rejected"

## Graph Structure
```
START → prepare → wait → [human decision]
                        ├→ approve → END
                        └→ reject → END
```

### Nodes:
1. **prepare**: Initializes the request
2. **wait**: Pauses for human input
3. **approve**: Processes approved request
4. **reject**: Handles rejected request

### Human Interaction Point:
- Workflow pauses at "wait" node
- UI displays request details
- User makes decision via buttons
- Decision is stored in state
- Graph resumes execution

## State Schema
```python
{
    "messages": list,        # Log of messages
    "current_step": str,     # Current workflow step
    "needs_approval": bool,  # Flag for approval requirement
    "user_response": str,    # User's decision
    "final_result": str      # Final outcome message
}
```

## UI Components
- Title and description
- Start workflow button
- Reset button
- Request details display
- Approve/Reject buttons (appear when waiting)
- Results display (after decision)
- Processing log
- Graph structure visualization
- Use cases examples

## Session State Management
- `workflow_state`: Tracks current state
- `workflow_started`: Boolean flag for active workflow
- Rerun after state changes to update UI

## Learning Objectives
- Understand human-in-the-loop patterns
- Learn to pause graph execution
- Implement user interaction points
- Practice session state management in Streamlit
- Handle asynchronous user input
- Build approval/rejection workflows
- Create interactive decision interfaces

## Workflow Scenarios
1. **Approval Path:**
   - Start → Prepare → Wait → [User Approves] → Process → Success
2. **Rejection Path:**
   - Start → Prepare → Wait → [User Rejects] → Reject → Cancelled

## Use Cases
- Approval workflows requiring manager sign-off
- Content moderation with human review
- AI decision support with human override
- Quality control checkpoints
- Compliance and audit requirements
