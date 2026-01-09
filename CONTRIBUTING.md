# Contributing to Learning LangGraph with Projects

Thank you for your interest in contributing! This document provides guidelines for contributing to this repository.

## 🤝 How to Contribute

### Ways to Contribute

1. **Report Bugs**: Found an issue? Open a bug report
2. **Suggest Enhancements**: Have an idea? Open a feature request
3. **Improve Documentation**: Fix typos, clarify instructions
4. **Add Examples**: Contribute new examples
5. **Improve Existing Examples**: Enhance current examples
6. **Add Tests**: Increase test coverage
7. **Generate Screenshots**: Create missing screenshots

## 📝 Adding a New Example

### Example Structure

Each example must include:

```
Example_XX_Name/
├── app.py              # Streamlit application
├── specifications.md   # Detailed specifications
└── test.py            # 10 unit tests
```

### Example Template

#### app.py

```python
import streamlit as st
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

# Define state
class ExampleState(TypedDict):
    input: str
    output: str
    steps: Annotated[list, operator.add]

# Define nodes
def process_node(state: ExampleState) -> ExampleState:
    """Process the input."""
    return {
        "output": f"Processed: {state['input']}",
        "steps": ["Processing completed"]
    }

# Create graph
def create_graph():
    workflow = StateGraph(ExampleState)
    workflow.add_node("process", process_node)
    workflow.set_entry_point("process")
    workflow.add_edge("process", END)
    return workflow.compile()

# Streamlit UI
st.title("🎯 Example Title")
st.markdown("### Example Description")

user_input = st.text_input("Enter input:")

if st.button("Process", type="primary"):
    graph = create_graph()
    result = graph.invoke({"input": user_input, "output": "", "steps": []})
    st.success("Complete!")
    st.write(f"Output: {result['output']}")

with st.expander("📊 Graph Structure"):
    st.markdown("```\nSTART → process → END\n```")
```

#### specifications.md

```markdown
# Example XX: Title

## Overview
Brief description of what this example demonstrates.

## What to Do
Step-by-step explanation of functionality.

## Inputs
- **Input Name**: Description
  - Type: data type
  - Example: example value

## Expected Outputs
- **Output Name**: Description
  - Format: output format
  - Example: example output

## Graph Structure
\```
START → node1 → node2 → END
\```

## State Schema
\```python
{
    "field": type,
    "another": type
}
\```

## Learning Objectives
- Key concept 1
- Key concept 2
- Key concept 3
```

#### test.py

```python
import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import ExampleState, process_node, create_graph

class TestExample:
    def test_node_basic(self):
        state = {"input": "test", "output": "", "steps": []}
        result = process_node(state)
        assert result["output"] is not None
    
    def test_graph_creation(self):
        graph = create_graph()
        assert graph is not None
    
    # Add 8 more tests...

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

### Guidelines

1. **Code Style**
   - Follow PEP 8
   - Use type hints
   - Add docstrings
   - Keep functions small and focused

2. **Documentation**
   - Clear and concise
   - Include examples
   - Explain complex concepts
   - Use proper markdown formatting

3. **Tests**
   - Minimum 10 tests per example
   - Test edge cases
   - Test error handling
   - Aim for high coverage

4. **UI/UX**
   - Clean and intuitive
   - Responsive layout
   - Clear error messages
   - Helpful tooltips

## 🧪 Testing Guidelines

### Before Submitting

```bash
# Run tests
pytest your_example/test.py -v

# Check code style (if using tools)
black your_example/app.py
pylint your_example/app.py

# Test the app works
streamlit run your_example/app.py
```

### Test Requirements

- All tests must pass
- Minimum 80% code coverage
- No syntax errors
- No import errors

## 📸 Screenshot Guidelines

When adding screenshots:

1. **Resolution**: 1280x720 or higher
2. **Format**: PNG
3. **Content**: Show app in use (after interaction)
4. **Quality**: Clear and readable text
5. **Location**: Save in example directory as `screenshot.png`

## 🔄 Pull Request Process

1. **Fork the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Learning_LangGraph_with-Projects.git
   cd Learning_LangGraph_with-Projects
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Add your example
   - Write tests
   - Update documentation

4. **Test Your Changes**
   ```bash
   pytest your_example/test.py -v
   streamlit run your_example/app.py
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add Example: Your Example Name"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New example
- [ ] Bug fix
- [ ] Documentation update
- [ ] Enhancement

## Testing
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] App runs without errors

## Screenshots
(If applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added
- [ ] Self-review completed
```

## 🐛 Bug Reports

When reporting bugs, include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: How to trigger the bug
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: 
   - OS
   - Python version
   - Package versions
6. **Screenshots**: If applicable
7. **Logs**: Error messages/stack traces

## 💡 Feature Requests

When suggesting features:

1. **Description**: Clear description of the feature
2. **Motivation**: Why this feature is needed
3. **Use Case**: How it would be used
4. **Examples**: Similar features elsewhere
5. **Implementation Ideas**: Possible approaches

## 📋 Code Review

All PRs will be reviewed for:

- **Functionality**: Does it work as intended?
- **Code Quality**: Is it clean and maintainable?
- **Documentation**: Is it well-documented?
- **Tests**: Are there adequate tests?
- **Style**: Does it follow guidelines?

## 🎯 Priority Areas

Currently seeking contributions in:

1. **Screenshots**: Generate screenshots for all examples
2. **Documentation**: Improve existing documentation
3. **Tests**: Add more comprehensive tests
4. **Examples**: Add more advanced examples
5. **Tutorials**: Create step-by-step tutorials

## ❓ Questions?

- Open an issue for questions
- Join community discussions
- Check existing issues and PRs

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing! 🙏
