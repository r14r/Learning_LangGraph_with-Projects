import pytest
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.dirname(__file__))
from app import AgentState, process_input, finalize_output, create_graph


class TestSimpleAgent:
    """Test suite for Simple Agent example"""
    
    def test_process_input_basic(self):
        """Test basic input processing"""
        state = {"input": "hello", "output": "", "steps": []}
        result = process_input(state)
        assert "Processed: HELLO" in result["output"]
        assert len(result["steps"]) == 1
        assert "Step 1" in result["steps"][0]
    
    def test_process_input_empty(self):
        """Test processing with empty input"""
        state = {"input": "", "output": "", "steps": []}
        result = process_input(state)
        assert result["output"] == "Processed: "
        assert len(result["steps"]) == 1
    
    def test_process_input_special_chars(self):
        """Test processing with special characters"""
        state = {"input": "test@123!", "output": "", "steps": []}
        result = process_input(state)
        assert result["output"] == "Processed: TEST@123!"
    
    def test_finalize_output_basic(self):
        """Test output finalization"""
        state = {"input": "test", "output": "Processed: TEST", "steps": []}
        result = finalize_output(state)
        assert result["output"] == "Processed: TEST [FINAL]"
        assert len(result["steps"]) == 1
        assert "Step 2" in result["steps"][0]
    
    def test_finalize_output_preserves_content(self):
        """Test that finalization preserves existing output"""
        state = {"input": "test", "output": "Some output", "steps": []}
        result = finalize_output(state)
        assert "Some output" in result["output"]
        assert result["output"].endswith(" [FINAL]")
    
    def test_graph_creation(self):
        """Test that graph is created successfully"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution_basic(self):
        """Test basic graph execution"""
        graph = create_graph()
        initial_state = {
            "input": "test",
            "output": "",
            "steps": []
        }
        result = graph.invoke(initial_state)
        assert "Processed: TEST [FINAL]" in result["output"]
        assert len(result["steps"]) == 2
    
    def test_graph_execution_multiple_words(self):
        """Test graph with multiple words"""
        graph = create_graph()
        initial_state = {
            "input": "hello world",
            "output": "",
            "steps": []
        }
        result = graph.invoke(initial_state)
        assert result["output"] == "Processed: HELLO WORLD [FINAL]"
    
    def test_graph_execution_steps_order(self):
        """Test that processing steps are in correct order"""
        graph = create_graph()
        initial_state = {
            "input": "test",
            "output": "",
            "steps": []
        }
        result = graph.invoke(initial_state)
        assert "Step 1" in result["steps"][0]
        assert "Step 2" in result["steps"][1]
    
    def test_graph_state_persistence(self):
        """Test that input is preserved in final state"""
        graph = create_graph()
        initial_state = {
            "input": "original input",
            "output": "",
            "steps": []
        }
        result = graph.invoke(initial_state)
        assert result["input"] == "original input"
        assert "ORIGINAL INPUT" in result["output"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
