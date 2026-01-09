import pytest
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import MathState, add_ten, multiply_by_two, subtract_five, create_graph


class TestBasicStateGraph:
    """Test suite for Basic State Graph example"""
    
    def test_add_ten_positive(self):
        """Test adding 10 to a positive number"""
        state = {"number": 5, "operations": [], "result": 5}
        result = add_ten(state)
        assert result["result"] == 15
        assert len(result["operations"]) == 1
        assert "15" in result["operations"][0]
    
    def test_add_ten_negative(self):
        """Test adding 10 to a negative number"""
        state = {"number": -3, "operations": [], "result": -3}
        result = add_ten(state)
        assert result["result"] == 7
    
    def test_multiply_by_two_basic(self):
        """Test multiplication by 2"""
        state = {"number": 5, "operations": [], "result": 15}
        result = multiply_by_two(state)
        assert result["result"] == 30
        assert "30" in result["operations"][0]
    
    def test_multiply_by_two_zero(self):
        """Test multiplication of zero"""
        state = {"number": 0, "operations": [], "result": 0}
        result = multiply_by_two(state)
        assert result["result"] == 0
    
    def test_subtract_five_basic(self):
        """Test subtracting 5"""
        state = {"number": 5, "operations": [], "result": 30}
        result = subtract_five(state)
        assert result["result"] == 25
        assert "25" in result["operations"][0]
    
    def test_graph_creation(self):
        """Test that graph is created successfully"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution_example1(self):
        """Test graph with input 5 (expected output 25)"""
        graph = create_graph()
        initial_state = {"number": 5, "operations": [], "result": 5}
        result = graph.invoke(initial_state)
        expected = ((5 + 10) * 2) - 5
        assert result["result"] == expected
        assert result["result"] == 25
    
    def test_graph_execution_example2(self):
        """Test graph with input 0 (expected output 15)"""
        graph = create_graph()
        initial_state = {"number": 0, "operations": [], "result": 0}
        result = graph.invoke(initial_state)
        expected = ((0 + 10) * 2) - 5
        assert result["result"] == expected
        assert result["result"] == 15
    
    def test_graph_execution_example3(self):
        """Test graph with input -3 (expected output 9)"""
        graph = create_graph()
        initial_state = {"number": -3, "operations": [], "result": -3}
        result = graph.invoke(initial_state)
        expected = ((-3 + 10) * 2) - 5
        assert result["result"] == expected
        assert result["result"] == 9
    
    def test_graph_operations_count(self):
        """Test that all three operations are recorded"""
        graph = create_graph()
        initial_state = {"number": 5, "operations": [], "result": 5}
        result = graph.invoke(initial_state)
        assert len(result["operations"]) == 3
        assert "Added 10" in result["operations"][0]
        assert "Multiplied by 2" in result["operations"][1]
        assert "Subtracted 5" in result["operations"][2]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
