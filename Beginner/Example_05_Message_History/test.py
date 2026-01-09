import pytest
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))
from app import ConversationState, greet_user, process_message, create_graph


class TestMessageHistory:
    """Test suite for Message History example"""
    
    def test_greet_user_basic(self):
        """Test basic greeting"""
        state = {"messages": [], "user_name": "Alice", "conversation_start": ""}
        result = greet_user(state)
        assert len(result["messages"]) == 1
        assert "Alice" in result["messages"][0]["content"]
        assert result["messages"][0]["role"] == "assistant"
    
    def test_greet_user_default(self):
        """Test greeting with no name"""
        state = {"messages": [], "user_name": "", "conversation_start": ""}
        result = greet_user(state)
        assert len(result["messages"]) == 1
        assert "User" in result["messages"][0]["content"]
    
    def test_process_message_hello(self):
        """Test processing hello message"""
        state = {
            "messages": [{"role": "user", "content": "hello", "timestamp": "10:00:00"}],
            "user_name": "Alice",
            "conversation_start": ""
        }
        result = process_message(state)
        assert len(result["messages"]) == 1
        assert "hello" in result["messages"][0]["content"].lower()
    
    def test_process_message_how_are_you(self):
        """Test processing how are you message"""
        state = {
            "messages": [{"role": "user", "content": "how are you", "timestamp": "10:00:00"}],
            "user_name": "Alice",
            "conversation_start": ""
        }
        result = process_message(state)
        assert "doing great" in result["messages"][0]["content"].lower()
    
    def test_process_message_goodbye(self):
        """Test processing goodbye message"""
        state = {
            "messages": [{"role": "user", "content": "bye", "timestamp": "10:00:00"}],
            "user_name": "Alice",
            "conversation_start": ""
        }
        result = process_message(state)
        assert "goodbye" in result["messages"][0]["content"].lower()
    
    def test_process_message_help(self):
        """Test processing help request"""
        state = {
            "messages": [{"role": "user", "content": "help me", "timestamp": "10:00:00"}],
            "user_name": "Alice",
            "conversation_start": ""
        }
        result = process_message(state)
        assert "help" in result["messages"][0]["content"].lower() or "can" in result["messages"][0]["content"].lower()
    
    def test_process_message_weather(self):
        """Test processing weather query"""
        state = {
            "messages": [{"role": "user", "content": "what's the weather", "timestamp": "10:00:00"}],
            "user_name": "Alice",
            "conversation_start": ""
        }
        result = process_message(state)
        assert "weather" in result["messages"][0]["content"].lower()
    
    def test_process_message_default(self):
        """Test processing unknown message"""
        state = {
            "messages": [{"role": "user", "content": "random text", "timestamp": "10:00:00"}],
            "user_name": "Alice",
            "conversation_start": ""
        }
        result = process_message(state)
        assert len(result["messages"]) == 1
        assert "random text" in result["messages"][0]["content"].lower()
    
    def test_graph_creation(self):
        """Test that graph is created successfully"""
        graph = create_graph()
        assert graph is not None
    
    def test_graph_execution_complete(self):
        """Test complete conversation flow"""
        graph = create_graph()
        initial_state = {
            "messages": [],
            "user_name": "Bob",
            "conversation_start": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        result = graph.invoke(initial_state)
        # Should have at least greeting message
        assert len(result["messages"]) >= 1
        assert result["messages"][0]["role"] == "assistant"
        assert "Bob" in result["messages"][0]["content"]
    
    def test_message_timestamp_exists(self):
        """Test that messages have timestamps"""
        state = {"messages": [], "user_name": "Alice", "conversation_start": ""}
        result = greet_user(state)
        assert "timestamp" in result["messages"][0]
        assert result["messages"][0]["timestamp"] is not None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
