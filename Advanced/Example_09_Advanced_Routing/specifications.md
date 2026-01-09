# Example 09: Advanced Routing

## Overview
Advanced level example demonstrating Complex routing patterns.

## What to Do
This example shows how to implement complex routing patterns in LangGraph.

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
- Understand complex routing patterns
- Practice graph construction
- Implement advanced-level patterns
