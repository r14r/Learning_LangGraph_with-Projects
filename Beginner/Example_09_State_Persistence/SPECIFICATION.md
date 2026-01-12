# Example 09: State Persistence

## Overview
Beginner level example demonstrating Saving and loading graph state.

## What to Do
This example shows how to implement saving and loading graph state in LangGraph.

## Inputs
- **User Input**: Text string
  - Type: String
  - Example: "test input"

## Expected Outputs
- **Processed Output**: Transformed input
- **Processing Steps**: List of operations performed

## Graph Structure
```
START → process → END
```

## State Schema
```python
{
    "input": str,
    "output": str,
    "steps": list
}
```

## Learning Objectives
- Understand saving and loading graph state
- Practice graph construction
- Implement beginner-level patterns
