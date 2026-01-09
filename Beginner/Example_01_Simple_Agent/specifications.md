# Example 01: Simple Agent

## Overview
A basic LangGraph agent that demonstrates sequential processing with two nodes.

## What to Do
This example creates a simple agent that:
1. Takes user input text
2. Processes it through a sequential graph with two nodes
3. Returns the transformed output along with processing steps

## Inputs
- **User Text Input**: Any string text entered by the user
  - Type: String
  - Example: "Hello LangGraph"
  - Constraints: Non-empty string

## Expected Outputs
- **Processed Output**: The input text transformed to uppercase with "[FINAL]" marker
  - Format: `"Processed: {INPUT_UPPERCASE} [FINAL]"`
  - Example: For input "Hello LangGraph", output is "Processed: HELLO LANGGRAPH [FINAL]"

- **Processing Steps**: A list showing the execution steps
  - Step 1: "Step 1: Received input '{user_input}'"
  - Step 2: "Step 2: Finalized output"

## Graph Structure
```
START → process → finalize → END
```

### Nodes:
1. **process**: 
   - Takes input text
   - Converts to uppercase
   - Wraps in "Processed: " prefix
   - Records step 1

2. **finalize**: 
   - Takes processed output
   - Adds " [FINAL]" suffix
   - Records step 2

## State Schema
```python
{
    "input": str,      # Original user input
    "output": str,     # Final processed output
    "steps": list      # List of processing steps
}
```

## UI Components
- Title and description
- Text input field for user input
- Process button to execute the graph
- Results display showing:
  - Input text
  - Output text
  - Processing steps
- Expandable section showing graph structure

## Learning Objectives
- Understand basic LangGraph StateGraph creation
- Learn how to define state structure with TypedDict
- Practice creating sequential node connections
- Use operator.add for list accumulation in state
- Implement simple node functions
- Build a Streamlit interface for LangGraph
