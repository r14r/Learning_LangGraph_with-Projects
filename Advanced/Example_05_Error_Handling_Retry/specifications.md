# Example 05: Error Handling & Retry

## Overview
Advanced level example demonstrating Robust error recovery.

## What to Do
This example shows how to implement robust error recovery in LangGraph.

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
- Understand robust error recovery
- Practice graph construction
- Implement advanced-level patterns
