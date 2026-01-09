# Example 03: Conditional Edges

## Overview
Demonstrates conditional routing in LangGraph based on input characteristics.

## What to Do
This example creates a graph with conditional edges that:
1. Classifies input numbers into categories (positive, negative, zero)
2. Routes to appropriate handlers based on classification
3. Processes each category differently
4. Returns results with routing information

## Inputs
- **Number**: Integer input for classification
  - Type: Integer
  - Range: -100 to 100
  - Default: 0
  - Examples: 42, 0, -15

## Expected Outputs
- **Classification**: Category of the number
  - Values: "positive", "negative", or "zero"
  - Based on: number > 0, number < 0, or number == 0

- **Route**: The handler path taken
  - Values: "positive", "negative", or "zero"
  - Matches the classification

- **Result**: Descriptive message about the number
  - Positive: "✅ {number} is positive! It's greater than zero."
  - Negative: "⚠️ {number} is negative! It's less than zero."
  - Zero: "⭕ {number} is zero! It's neither positive nor negative."

- **Operations**: List of processing steps
  - Step 1: Classification operation
  - Step 2: Handler operation

## Graph Structure
```
START → classify → [conditional routing]
                 ├→ positive → END
                 ├→ negative → END
                 └→ zero → END
```

### Nodes:
1. **classify**: Determines the category of the number
2. **positive**: Handles positive numbers
3. **negative**: Handles negative numbers
4. **zero**: Handles zero

### Conditional Routing:
- Uses `route_number()` function to determine path
- Returns literal type indicating which node to visit
- Based on the "classification" field in state

## State Schema
```python
{
    "number": int,          # Input number
    "classification": str,  # Category (positive/negative/zero)
    "route": str,          # Path taken through graph
    "operations": list,    # Log of operations
    "result": str          # Final message
}
```

## UI Components
- Title and description
- Number input with live classification preview
- Process button
- Results display showing:
  - Input number
  - Classification
  - Route taken
  - Result message
  - Processing steps
- Graph structure diagram
- Example table with test cases

## Learning Objectives
- Understand conditional edges in LangGraph
- Learn how to implement routing functions
- Use Literal type hints for routing
- Practice creating multiple handler nodes
- Implement classification logic
- Build conditional UI feedback
- Handle multiple execution paths

## Routing Examples
| Input | Classification | Route | Handler |
|-------|---------------|-------|---------|
| 42    | positive      | positive | handle_positive |
| 1     | positive      | positive | handle_positive |
| 0     | zero          | zero | handle_zero |
| -1    | negative      | negative | handle_negative |
| -42   | negative      | negative | handle_negative |
