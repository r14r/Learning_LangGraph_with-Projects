import pytest
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import (
    ClassificationState, classify_number, handle_positive, 
    handle_negative, handle_zero, route_number, create_graph
)


class TestConditionalEdges:
    """Test suite for Conditional Edges example"""
    
    def test_classify_positive(self):
        """Test classification of positive number"""
        state = {"number": 42, "classification": "", "route": "", "operations": [], "result": ""}
        result = classify_number(state)
        assert result["classification"] == "positive"
        assert len(result["operations"]) == 1
    
    def test_classify_negative(self):
        """Test classification of negative number"""
        state = {"number": -15, "classification": "", "route": "", "operations": [], "result": ""}
        result = classify_number(state)
        assert result["classification"] == "negative"
    
    def test_classify_zero(self):
        """Test classification of zero"""
        state = {"number": 0, "classification": "", "route": "", "operations": [], "result": ""}
        result = classify_number(state)
        assert result["classification"] == "zero"
    
    def test_handle_positive(self):
        """Test positive number handler"""
        state = {"number": 10, "classification": "positive", "route": "", "operations": [], "result": ""}
        result = handle_positive(state)
        assert result["route"] == "positive"
        assert "10" in result["result"]
        assert "positive" in result["result"]
    
    def test_handle_negative(self):
        """Test negative number handler"""
        state = {"number": -5, "classification": "negative", "route": "", "operations": [], "result": ""}
        result = handle_negative(state)
        assert result["route"] == "negative"
        assert "-5" in result["result"]
        assert "negative" in result["result"]
    
    def test_handle_zero(self):
        """Test zero handler"""
        state = {"number": 0, "classification": "zero", "route": "", "operations": [], "result": ""}
        result = handle_zero(state)
        assert result["route"] == "zero"
        assert "zero" in result["result"].lower()
    
    def test_route_positive(self):
        """Test routing for positive classification"""
        state = {"number": 5, "classification": "positive", "route": "", "operations": [], "result": ""}
        route = route_number(state)
        assert route == "positive"
    
    def test_route_negative(self):
        """Test routing for negative classification"""
        state = {"number": -5, "classification": "negative", "route": "", "operations": [], "result": ""}
        route = route_number(state)
        assert route == "negative"
    
    def test_graph_execution_positive(self):
        """Test complete graph execution with positive number"""
        graph = create_graph()
        initial_state = {
            "number": 42,
            "classification": "",
            "route": "",
            "operations": [],
            "result": ""
        }
        result = graph.invoke(initial_state)
        assert result["classification"] == "positive"
        assert result["route"] == "positive"
        assert "42" in result["result"]
        assert len(result["operations"]) == 2
    
    def test_graph_execution_zero(self):
        """Test complete graph execution with zero"""
        graph = create_graph()
        initial_state = {
            "number": 0,
            "classification": "",
            "route": "",
            "operations": [],
            "result": ""
        }
        result = graph.invoke(initial_state)
        assert result["classification"] == "zero"
        assert result["route"] == "zero"
        assert len(result["operations"]) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
