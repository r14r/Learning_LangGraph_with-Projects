# Example 03: Subgraphs

## Overview
Advanced level example demonstrating Nested graph structures.

## What to Do
This example shows how to implement nested graph structures in LangGraph.

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
- Understand nested graph structures
- Practice graph construction
- Implement advanced-level patterns
