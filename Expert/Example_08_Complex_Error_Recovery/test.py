import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import ExampleState, process_node, create_graph


class TestComplexErrorRecovery:
    """Test suite for Complex Error Recovery example"""
    
    def test_process_node_basic(self):
        """Test basic processing"""
        state = {"input": "test", "output": "", "steps": []}
        result = process_node(state)
        assert "test" in result["output"].lower()
        assert len(result["steps"]) == 1
    
    def test_process_node_empty(self):
        """Test with empty input"""
        state = {"input": "", "output": "", "steps": []}
        result = process_node(state)
        assert result["output"] is not None
    
    def test_graph_creation(self):
        """Test graph creation"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution(self):
        """Test graph execution"""
        graph = create_graph()
        result = graph.invoke({"input": "test", "output": "", "steps": []})
        assert result["output"] is not None
        assert len(result["steps"]) >= 1
    
    def test_input_preserved(self):
        """Test input preservation"""
        graph = create_graph()
        result = graph.invoke({"input": "test123", "output": "", "steps": []})
        assert result["input"] == "test123"
    
    def test_output_format(self):
        """Test output format"""
        graph = create_graph()
        result = graph.invoke({"input": "test", "output": "", "steps": []})
        assert isinstance(result["output"], str)
    
    def test_steps_accumulation(self):
        """Test steps are accumulated"""
        state = {"input": "test", "output": "", "steps": []}
        result = process_node(state)
        assert isinstance(result["steps"], list)
    
    def test_multiple_inputs(self):
        """Test with various inputs"""
        graph = create_graph()
        for inp in ["test1", "test2", "test3"]:
            result = graph.invoke({"input": inp, "output": "", "steps": []})
            assert inp in result["output"].lower()
    
    def test_state_structure(self):
        """Test state structure"""
        graph = create_graph()
        result = graph.invoke({"input": "test", "output": "", "steps": []})
        assert "input" in result
        assert "output" in result
        assert "steps" in result
    
    def test_steps_content(self):
        """Test steps content"""
        state = {"input": "test", "output": "", "steps": []}
        result = process_node(state)
        assert len(result["steps"]) > 0
        assert isinstance(result["steps"][0], str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
