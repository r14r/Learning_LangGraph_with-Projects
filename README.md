# Learning LangGraph with Projects

A comprehensive collection of **30 Streamlit examples** demonstrating LangGraph capabilities across three skill levels: Beginner, Advanced, and Expert.

## 📚 Overview

This repository provides hands-on learning materials for LangGraph through interactive Streamlit applications. Each example includes:
- ✅ **Runnable Streamlit app** (`app.py`)
- 📝 **Detailed specifications** (`specifications.md`)
- 🧪 **10 comprehensive tests** (`test.py`)
- 📸 **Screenshot** (see screenshots/ directory)

## 🎯 Structure

```
├── Beginner/           # 10 foundational examples
├── Advanced/           # 10 intermediate examples
├── Expert/             # 10 advanced examples
└── requirements.txt    # Dependencies
```

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/r14r/Learning_LangGraph_with-Projects.git
cd Learning_LangGraph_with-Projects

# Install dependencies
pip install -r requirements.txt
```

### Running Examples

```bash
# Run any example
streamlit run Beginner/Example_01_Simple_Agent/app.py

# Or navigate to specific example
cd Beginner/Example_01_Simple_Agent
streamlit run app.py
```

### Running Tests

```bash
# Test a specific example
cd Beginner/Example_01_Simple_Agent
pytest test.py -v

# Test all examples in a level
pytest Beginner/*/test.py -v
```

## 📖 Examples

### 🟢 Beginner Level (10 Examples)

| # | Example | Description |
|---|---------|-------------|
| 01 | **Simple Agent** | Basic agent with sequential processing |
| 02 | **Basic State Graph** | Sequential mathematical operations |
| 03 | **Conditional Edges** | Routing based on conditions |
| 04 | **Human-in-the-Loop** | Interactive approval workflow |
| 05 | **Message History** | Conversation with memory |
| 06 | **Simple Chatbot** | Intent-based chat system |
| 07 | **Tool Calling** | Using tools in LangGraph |
| 08 | **Multi-Step Workflow** | Sequential processing pipeline |
| 09 | **State Persistence** | Saving and loading graph state |
| 10 | **Basic Router** | Simple message routing system |

### 🟡 Advanced Level (10 Examples)

| # | Example | Description |
|---|---------|-------------|
| 01 | **Complex State Management** | Advanced state handling patterns |
| 02 | **Parallel Processing** | Concurrent node execution |
| 03 | **Subgraphs** | Nested graph structures |
| 04 | **Custom Checkpointing** | State checkpoint management |
| 05 | **Error Handling & Retry** | Robust error recovery |
| 06 | **Streaming Responses** | Real-time output streaming |
| 07 | **Multi-Agent Collaboration** | Multiple agents working together |
| 08 | **Dynamic Graph Construction** | Runtime graph building |
| 09 | **Advanced Routing** | Complex routing patterns |
| 10 | **Time-based Workflows** | Scheduled and timed operations |

### 🔴 Expert Level (10 Examples)

| # | Example | Description |
|---|---------|-------------|
| 01 | **Hierarchical Agent Systems** | Multi-level agent architecture |
| 02 | **Custom State Serialization** | Advanced state persistence |
| 03 | **Production Deployment** | Enterprise deployment strategies |
| 04 | **Advanced Memory Systems** | Sophisticated memory management |
| 05 | **Distributed Graph Execution** | Distributed processing |
| 06 | **Custom Middleware** | Graph middleware patterns |
| 07 | **Graph Optimization** | Performance optimization techniques |
| 08 | **Complex Error Recovery** | Advanced error handling |
| 09 | **Multi-Modal Agents** | Agents handling multiple data types |
| 10 | **Enterprise Integration** | Integration with enterprise systems |

## 📁 Example Structure

Each example follows this structure:

```
Example_XX_Name/
├── app.py              # Streamlit application
├── specifications.md   # Detailed specifications
├── test.py            # 10 unit tests
└── screenshot.png     # UI screenshot
```

### specifications.md Contents

Each specification file includes:
- **Overview**: What the example demonstrates
- **What to Do**: Step-by-step functionality
- **Inputs**: Expected input parameters
- **Expected Outputs**: What the example produces
- **Graph Structure**: Visual representation of the graph
- **State Schema**: Data structure definitions
- **Learning Objectives**: Key takeaways

### test.py Contents

Each test file includes 10 tests covering:
- Individual node functions
- Graph creation
- Complete graph execution
- Edge cases
- State management
- Input/output validation

## 🛠️ Technologies

- **LangGraph**: Graph-based agent framework
- **Streamlit**: Interactive web applications
- **LangChain**: LLM application framework
- **LangChain-Core**: 1.2.5 (patched for security vulnerabilities)
- **Python 3.8+**: Programming language
- **Pytest**: Testing framework

### Security Notes

This repository uses **langchain-core 1.2.5** which includes security patches for:
- Template injection vulnerabilities (CVE-2024-XXXX)
- Serialization injection vulnerabilities
- Attribute access security issues

Always keep dependencies updated to the latest patched versions.

## 📚 Learning Path

### Recommended Order

1. **Start with Beginner** (Examples 01-10)
   - Master basic concepts
   - Understand state management
   - Learn graph construction

2. **Progress to Advanced** (Examples 01-10)
   - Explore complex patterns
   - Handle errors and retries
   - Work with multiple agents

3. **Master Expert** (Examples 01-10)
   - Production-ready patterns
   - Optimization techniques
   - Enterprise integration

## 🧪 Testing

All examples include comprehensive test coverage:

```bash
# Run all tests
pytest */*/test.py -v

# Run tests for specific level
pytest Beginner/*/test.py -v
pytest Advanced/*/test.py -v
pytest Expert/*/test.py -v

# Run specific example tests
pytest Beginner/Example_01_Simple_Agent/test.py -v
```

## 📸 Screenshots

Screenshots for all examples are available in the `screenshots/` directory (to be generated).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [LangChain Documentation](https://python.langchain.com/)

## 🙏 Acknowledgments

This repository was created as a comprehensive learning resource for the LangGraph community.

---

**Happy Learning! 🚀**