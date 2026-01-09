import pytest
import math
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import ToolState, calculator, string_tool, parse_query, execute_tool, create_graph


class TestToolCalling:
    """Test suite for Tool Calling example"""
    
    def test_calculator_add(self):
        """Test calculator addition"""
        result = calculator("add", 10, 5)
        assert result == 15
    
    def test_calculator_subtract(self):
        """Test calculator subtraction"""
        result = calculator("subtract", 10, 5)
        assert result == 5
    
    def test_calculator_multiply(self):
        """Test calculator multiplication"""
        result = calculator("multiply", 10, 5)
        assert result == 50
    
    def test_calculator_divide(self):
        """Test calculator division"""
        result = calculator("divide", 10, 5)
        assert result == 2
    
    def test_calculator_divide_by_zero(self):
        """Test calculator division by zero"""
        result = calculator("divide", 10, 0)
        assert "Error" in str(result)
    
    def test_calculator_power(self):
        """Test calculator power operation"""
        result = calculator("power", 2, 3)
        assert result == 8
    
    def test_calculator_sqrt(self):
        """Test calculator square root"""
        result = calculator("sqrt", 16, 0)
        assert result == 4
    
    def test_string_tool_uppercase(self):
        """Test string uppercase"""
        result = string_tool("uppercase", "hello")
        assert result == "HELLO"
    
    def test_string_tool_lowercase(self):
        """Test string lowercase"""
        result = string_tool("lowercase", "HELLO")
        assert result == "hello"
    
    def test_string_tool_reverse(self):
        """Test string reverse"""
        result = string_tool("reverse", "hello")
        assert result == "olleh"
    
    def test_string_tool_length(self):
        """Test string length"""
        result = string_tool("length", "hello")
        assert "5" in result
    
    def test_parse_query_calculator(self):
        """Test query parsing for calculator"""
        state = {"query": "calculate add two numbers", "tool_calls": [], "result": ""}
        result = parse_query(state)
        assert len(result["tool_calls"]) == 1
        assert result["tool_calls"][0]["tool"] == "calculator"
    
    def test_parse_query_string(self):
        """Test query parsing for string tool"""
        state = {"query": "convert text to uppercase", "tool_calls": [], "result": ""}
        result = parse_query(state)
        assert len(result["tool_calls"]) == 1
        assert result["tool_calls"][0]["tool"] == "string"
    
    def test_graph_creation(self):
        """Test that graph is created successfully"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution(self):
        """Test complete graph execution"""
        graph = create_graph()
        state = {"query": "calculate something", "tool_calls": [], "result": ""}
        result = graph.invoke(state)
        assert len(result["tool_calls"]) >= 1
        assert result["result"] is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
