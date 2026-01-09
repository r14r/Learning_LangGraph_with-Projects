# Quick Start Guide

## Installation

```bash
# Clone the repository
git clone https://github.com/r14r/Learning_LangGraph_with-Projects.git
cd Learning_LangGraph_with-Projects

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Examples

### Run a Single Example

```bash
# Navigate to an example directory
cd Beginner/Example_01_Simple_Agent

# Run the Streamlit app
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Run Different Examples

```bash
# Beginner examples
streamlit run Beginner/Example_01_Simple_Agent/app.py
streamlit run Beginner/Example_02_Basic_State_Graph/app.py
streamlit run Beginner/Example_03_Conditional_Edges/app.py

# Advanced examples
streamlit run Advanced/Example_01_Complex_State_Management/app.py
streamlit run Advanced/Example_02_Parallel_Processing/app.py

# Expert examples
streamlit run Expert/Example_01_Hierarchical_Agent_Systems/app.py
```

## Testing Examples

### Test a Single Example

```bash
cd Beginner/Example_01_Simple_Agent
pytest test.py -v
```

### Test All Examples in a Level

```bash
# Test all Beginner examples
pytest Beginner/*/test.py -v

# Test all Advanced examples
pytest Advanced/*/test.py -v

# Test all Expert examples
pytest Expert/*/test.py -v
```

### Test Everything

```bash
pytest */*/test.py -v
```

## Learning Path

### Day 1-3: Beginner Level
Start with the fundamentals:

1. **Example 01 - Simple Agent**: Understand basic graph structure
2. **Example 02 - Basic State Graph**: Learn state management
3. **Example 03 - Conditional Edges**: Master routing logic
4. **Example 04 - Human-in-the-Loop**: Interactive workflows
5. **Example 05 - Message History**: Conversation memory
6. **Example 06 - Simple Chatbot**: Intent recognition
7. **Example 07 - Tool Calling**: External tool integration
8. **Example 08 - Multi-Step Workflow**: Sequential processing
9. **Example 09 - State Persistence**: Save and load state
10. **Example 10 - Basic Router**: Message routing

### Day 4-7: Advanced Level
Build on the fundamentals:

1. **Example 01 - Complex State Management**: Advanced patterns
2. **Example 02 - Parallel Processing**: Concurrent execution
3. **Example 03 - Subgraphs**: Nested structures
4. **Example 04 - Custom Checkpointing**: State management
5. **Example 05 - Error Handling & Retry**: Robust systems
6. **Example 06 - Streaming Responses**: Real-time output
7. **Example 07 - Multi-Agent Collaboration**: Agent coordination
8. **Example 08 - Dynamic Graph Construction**: Runtime graphs
9. **Example 09 - Advanced Routing**: Complex patterns
10. **Example 10 - Time-based Workflows**: Scheduled operations

### Day 8-10: Expert Level
Master production patterns:

1. **Example 01 - Hierarchical Agent Systems**: Multi-level architecture
2. **Example 02 - Custom State Serialization**: Advanced persistence
3. **Example 03 - Production Deployment**: Enterprise patterns
4. **Example 04 - Advanced Memory Systems**: Sophisticated memory
5. **Example 05 - Distributed Graph Execution**: Distributed processing
6. **Example 06 - Custom Middleware**: Middleware patterns
7. **Example 07 - Graph Optimization**: Performance tuning
8. **Example 08 - Complex Error Recovery**: Advanced error handling
9. **Example 09 - Multi-Modal Agents**: Multiple data types
10. **Example 10 - Enterprise Integration**: System integration

## Common Commands

### Development

```bash
# Format code (if using black)
black Beginner/Example_01_Simple_Agent/app.py

# Type checking (if using mypy)
mypy Beginner/Example_01_Simple_Agent/app.py

# Linting (if using pylint)
pylint Beginner/Example_01_Simple_Agent/app.py
```

### Streamlit Options

```bash
# Run on a different port
streamlit run app.py --server.port 8502

# Run without opening browser
streamlit run app.py --server.headless true

# Enable development mode
streamlit run app.py --server.runOnSave true
```

## Troubleshooting

### Port Already in Use

```bash
# Kill process on port 8501
lsof -ti:8501 | xargs kill -9  # Linux/Mac
netstat -ano | findstr :8501   # Windows (find PID then kill)
```

### Module Not Found

```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Import Errors

```bash
# Make sure you're in the correct directory
cd /path/to/Learning_LangGraph_with-Projects

# Verify installation
pip list | grep langgraph
pip list | grep streamlit
```

## Tips

1. **Start Simple**: Begin with Beginner examples even if experienced
2. **Run Tests First**: Understand expected behavior from tests
3. **Read Specifications**: Review specs before running examples
4. **Experiment**: Modify code and see what happens
5. **Take Notes**: Document your learning journey

## Next Steps

- Join the community discussions
- Contribute your own examples
- Share your learnings
- Build your own projects

## Resources

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [LangChain Docs](https://python.langchain.com/)
