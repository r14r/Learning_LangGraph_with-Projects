# Example 07: Tool Calling

## Overview
Demonstrates tool calling patterns in LangGraph with calculator and string manipulation tools.

## What to Do
This example creates a tool-calling system that:
1. Parses user queries to identify required tools
2. Routes to appropriate tool handlers
3. Executes tools with provided parameters
4. Returns results to the user

## Inputs
- **Calculator Tool Inputs:**
  - First number: Float (-∞ to +∞)
  - Operation: "add", "subtract", "multiply", "divide", "power", "sqrt"
  - Second number: Float (-∞ to +∞)

- **String Tool Inputs:**
  - Text: Any string
  - Operation: "uppercase", "lowercase", "reverse", "length", "capitalize"

## Expected Outputs
- **Calculator Results:**
  - add: a + b
  - subtract: a - b
  - multiply: a * b
  - divide: a / b (or error if b=0)
  - power: a ** b
  - sqrt: √a

- **String Tool Results:**
  - uppercase: Text in ALL CAPS
  - lowercase: text in lowercase
  - reverse: txet desrever
  - length: "Length: N"
  - capitalize: First letter uppercase

- **Tool Calls Log:** List of tools invoked with their queries

## Graph Structure
```
START → parse → execute → END
```

### Nodes:
1. **parse**: Query analysis and tool selection
2. **execute**: Tool invocation with parameters

## State Schema
```python
{
    "query": str,          # User query
    "tool_calls": list,    # Log of tool invocations
    "result": str          # Execution result
}
```

## Available Tools

### Calculator Tool
- **add(a, b)**: Addition
- **subtract(a, b)**: Subtraction
- **multiply(a, b)**: Multiplication
- **divide(a, b)**: Division (with zero check)
- **power(a, b)**: Exponentiation
- **sqrt(a, _)**: Square root

### String Tool
- **uppercase(text)**: Convert to uppercase
- **lowercase(text)**: Convert to lowercase
- **reverse(text)**: Reverse string
- **length(text)**: Get string length
- **capitalize(text)**: Capitalize first letter

## UI Components
- Tool type selector (radio buttons)
- Calculator interface:
  - Number inputs
  - Operation dropdown
  - Calculate button
- String tool interface:
  - Text input
  - Operation dropdown
  - Process button
- Results display
- Tool calls log
- Graph structure
- Example queries

## Learning Objectives
- Understand tool calling patterns
- Learn tool selection logic
- Practice function routing
- Implement parameter passing
- Handle multiple tool types
- Build tool interfaces
- Create interactive tool UIs

## Example Usage
| Tool | Operation | Input | Output |
|------|-----------|-------|--------|
| Calculator | add | 10, 5 | 15 |
| Calculator | multiply | 10, 5 | 50 |
| Calculator | power | 2, 3 | 8 |
| String | uppercase | "hello" | "HELLO" |
| String | reverse | "hello" | "olleh" |
| String | length | "hello" | "Length: 5" |
