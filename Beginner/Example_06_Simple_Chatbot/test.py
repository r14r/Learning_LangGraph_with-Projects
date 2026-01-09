import pytest
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import ChatState, understand_intent, generate_response, create_graph


class TestSimpleChatbot:
    """Test suite for Simple Chatbot example"""
    
    def test_understand_greeting(self):
        """Test greeting intent recognition"""
        state = {
            "messages": [{"role": "user", "content": "Hello there!", "timestamp": "10:00:00"}],
            "context": {}
        }
        result = understand_intent(state)
        assert result["context"]["intent"] == "greeting"
    
    def test_understand_farewell(self):
        """Test farewell intent recognition"""
        state = {
            "messages": [{"role": "user", "content": "Goodbye!", "timestamp": "10:00:00"}],
            "context": {}
        }
        result = understand_intent(state)
        assert result["context"]["intent"] == "farewell"
    
    def test_understand_question(self):
        """Test question intent recognition"""
        state = {
            "messages": [{"role": "user", "content": "What can you do?", "timestamp": "10:00:00"}],
            "context": {}
        }
        result = understand_intent(state)
        assert result["context"]["intent"] == "question"
    
    def test_understand_gratitude(self):
        """Test gratitude intent recognition"""
        state = {
            "messages": [{"role": "user", "content": "Thank you!", "timestamp": "10:00:00"}],
            "context": {}
        }
        result = understand_intent(state)
        assert result["context"]["intent"] == "gratitude"
    
    def test_understand_statement(self):
        """Test statement intent recognition"""
        state = {
            "messages": [{"role": "user", "content": "I like chatbots", "timestamp": "10:00:00"}],
            "context": {}
        }
        result = understand_intent(state)
        assert result["context"]["intent"] == "statement"
    
    def test_generate_response_greeting(self):
        """Test greeting response generation"""
        state = {
            "messages": [],
            "context": {"intent": "greeting", "last_user_msg": "Hello"}
        }
        result = generate_response(state)
        assert len(result["messages"]) == 1
        assert result["messages"][0]["role"] == "assistant"
        assert "hello" in result["messages"][0]["content"].lower()
    
    def test_generate_response_farewell(self):
        """Test farewell response generation"""
        state = {
            "messages": [],
            "context": {"intent": "farewell", "last_user_msg": "Bye"}
        }
        result = generate_response(state)
        assert "goodbye" in result["messages"][0]["content"].lower()
    
    def test_generate_response_question(self):
        """Test question response generation"""
        state = {
            "messages": [],
            "context": {"intent": "question", "last_user_msg": "What can you do?"}
        }
        result = generate_response(state)
        assert "question" in result["messages"][0]["content"].lower()
    
    def test_graph_creation(self):
        """Test that graph is created successfully"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution_complete(self):
        """Test complete chat interaction"""
        graph = create_graph()
        initial_state = {
            "messages": [{"role": "user", "content": "Hello!", "timestamp": "10:00:00"}],
            "context": {}
        }
        result = graph.invoke(initial_state)
        assert len(result["messages"]) >= 1
        # Should have assistant response
        assistant_msgs = [m for m in result["messages"] if m["role"] == "assistant"]
        assert len(assistant_msgs) >= 1
        assert assistant_msgs[-1]["intent"] == "greeting"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
