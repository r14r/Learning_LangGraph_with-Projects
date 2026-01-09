import pytest
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import (
    InteractionState, prepare_request, wait_for_human,
    process_approval, process_rejection, check_approval, create_graph
)


class TestHumanInTheLoop:
    """Test suite for Human-in-the-Loop example"""
    
    def test_prepare_request(self):
        """Test request preparation"""
        state = {"messages": [], "current_step": "", "needs_approval": False, "user_response": "", "final_result": ""}
        result = prepare_request(state)
        assert result["current_step"] == "prepared"
        assert result["needs_approval"] == True
        assert len(result["messages"]) == 1
    
    def test_wait_for_human(self):
        """Test waiting state"""
        state = {"messages": [], "current_step": "", "needs_approval": True, "user_response": "", "final_result": ""}
        result = wait_for_human(state)
        assert result["current_step"] == "waiting"
        assert "waiting" in result["messages"][0].lower()
    
    def test_process_approval(self):
        """Test approval processing"""
        state = {"messages": [], "current_step": "waiting", "needs_approval": True, "user_response": "approve", "final_result": ""}
        result = process_approval(state)
        assert result["current_step"] == "approved"
        assert "approved" in result["final_result"].lower()
        assert "✅" in result["final_result"]
    
    def test_process_rejection(self):
        """Test rejection processing"""
        state = {"messages": [], "current_step": "waiting", "needs_approval": True, "user_response": "reject", "final_result": ""}
        result = process_rejection(state)
        assert result["current_step"] == "rejected"
        assert "rejected" in result["final_result"].lower()
        assert "❌" in result["final_result"]
    
    def test_check_approval_approved(self):
        """Test routing with approval"""
        state = {"messages": [], "current_step": "waiting", "needs_approval": True, "user_response": "approve", "final_result": ""}
        route = check_approval(state)
        assert route == "approved"
    
    def test_check_approval_rejected(self):
        """Test routing with rejection"""
        state = {"messages": [], "current_step": "waiting", "needs_approval": True, "user_response": "reject", "final_result": ""}
        route = check_approval(state)
        assert route == "rejected"
    
    def test_check_approval_default(self):
        """Test routing with no response defaults to rejection"""
        state = {"messages": [], "current_step": "waiting", "needs_approval": True, "user_response": "", "final_result": ""}
        route = check_approval(state)
        assert route == "rejected"
    
    def test_graph_creation(self):
        """Test that graph is created successfully"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution_approval_path(self):
        """Test complete graph execution with approval"""
        graph = create_graph()
        initial_state = {
            "messages": [],
            "current_step": "initial",
            "needs_approval": False,
            "user_response": "approve",
            "final_result": ""
        }
        result = graph.invoke(initial_state)
        assert result["current_step"] == "approved"
        assert "approved" in result["final_result"].lower()
        assert len(result["messages"]) >= 3
    
    def test_graph_execution_rejection_path(self):
        """Test complete graph execution with rejection"""
        graph = create_graph()
        initial_state = {
            "messages": [],
            "current_step": "initial",
            "needs_approval": False,
            "user_response": "reject",
            "final_result": ""
        }
        result = graph.invoke(initial_state)
        assert result["current_step"] == "rejected"
        assert "rejected" in result["final_result"].lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
