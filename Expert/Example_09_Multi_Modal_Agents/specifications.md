# Example 09: Multi-Modal Agents

## Overview
Expert level example demonstrating Agents handling multiple data types.

## What to Do
This example shows how to implement agents handling multiple data types in LangGraph.

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
- Understand agents handling multiple data types
- Practice graph construction
- Implement expert-level patterns
