# Example 10: Basic Router

## Overview
Beginner level example demonstrating Simple message routing system.

## What to Do
This example shows how to implement simple message routing system in LangGraph.

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
- Understand simple message routing system
- Practice graph construction
- Implement beginner-level patterns
