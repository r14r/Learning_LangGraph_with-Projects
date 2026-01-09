# Example 02: Basic State Graph

## Overview
Demonstrates state management in LangGraph through sequential mathematical operations.

## What to Do
This example creates a state graph that:
1. Takes a numeric input
2. Applies three mathematical operations in sequence
3. Tracks each operation and maintains state
4. Returns the final result with operation history

## Inputs
- **Number**: Integer input for calculations
  - Type: Integer
  - Range: -1000 to 1000
  - Default: 5
  - Example: 5, 0, -3, 10

## Expected Outputs
- **Final Result**: The result after all operations
  - Formula: `((number + 10) * 2) - 5`
  - Example: For input 5, result is 25
    - Step 1: 5 + 10 = 15
    - Step 2: 15 * 2 = 30
    - Step 3: 30 - 5 = 25

- **Operations List**: Detailed log of each operation
  - Format: List of strings describing each step
  - Example:
    ```
    ["Added 10: 5 + 10 = 15",
     "Multiplied by 2: 15 * 2 = 30",
     "Subtracted 5: 30 - 5 = 25"]
    ```

## Graph Structure
```
START → add → multiply → subtract → END
```

### Nodes:
1. **add**: Adds 10 to the input number
2. **multiply**: Multiplies current result by 2
3. **subtract**: Subtracts 5 from current result

## State Schema
```python
{
    "number": int,        # Original input number
    "operations": list,   # Log of operations performed
    "result": int         # Current/final result
}
```

## UI Components
- Title and description with formula
- Number input field with validation
- Quick test showing expected result
- Calculate button
- Results display:
  - Initial number
  - Final result
  - Step-by-step operations
  - Verification status
- Graph structure visualization
- Example calculations table

## Learning Objectives
- Understand state persistence across nodes
- Learn how to maintain operation history
- Practice sequential edge connections
- Implement mathematical transformations
- Use annotated types for list accumulation
- Validate graph execution results
- Build interactive number-based UI

## Test Cases Examples
- Input: 5 → Output: 25
- Input: 0 → Output: 15
- Input: -3 → Output: 9
- Input: 10 → Output: 35
