# Example 06: Custom Middleware

## Overview
Expert level example demonstrating Graph middleware patterns.

## What to Do
This example shows how to implement graph middleware patterns in LangGraph.

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
- Understand graph middleware patterns
- Practice graph construction
- Implement expert-level patterns
