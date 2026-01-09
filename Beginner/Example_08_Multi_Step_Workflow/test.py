import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import WorkflowState, step1_collect_data, step2_validate_data, step3_process_data, step4_save_results, create_graph


class TestMultiStepWorkflow:
    """Test suite for Multi-Step Workflow example"""
    
    def test_step1(self):
        state = {"data": {}, "steps_completed": [], "status": ""}
        result = step1_collect_data(state)
        assert len(result["steps_completed"]) == 1
        assert "Step 1" in result["steps_completed"][0]
    
    def test_step2(self):
        state = {"data": {}, "steps_completed": [], "status": ""}
        result = step2_validate_data(state)
        assert "Step 2" in result["steps_completed"][0]
    
    def test_step3(self):
        state = {"data": {}, "steps_completed": [], "status": ""}
        result = step3_process_data(state)
        assert "Step 3" in result["steps_completed"][0]
    
    def test_step4(self):
        state = {"data": {}, "steps_completed": [], "status": ""}
        result = step4_save_results(state)
        assert "Step 4" in result["steps_completed"][0]
        assert result["status"] == "completed"
    
    def test_graph_creation(self):
        graph = create_graph()
        assert graph is not None
    
    def test_complete_workflow(self):
        graph = create_graph()
        result = graph.invoke({"data": {}, "steps_completed": [], "status": "started"})
        assert len(result["steps_completed"]) == 4
        assert result["status"] == "completed"
    
    def test_workflow_order(self):
        graph = create_graph()
        result = graph.invoke({"data": {}, "steps_completed": [], "status": "started"})
        assert "Step 1" in result["steps_completed"][0]
        assert "Step 2" in result["steps_completed"][1]
        assert "Step 3" in result["steps_completed"][2]
        assert "Step 4" in result["steps_completed"][3]
    
    def test_workflow_with_data(self):
        graph = create_graph()
        result = graph.invoke({"data": {"input": "test"}, "steps_completed": [], "status": "started"})
        assert result["data"]["input"] == "test"
    
    def test_status_progression(self):
        graph = create_graph()
        result = graph.invoke({"data": {}, "steps_completed": [], "status": "started"})
        assert result["status"] == "completed"
    
    def test_steps_accumulated(self):
        graph = create_graph()
        result = graph.invoke({"data": {}, "steps_completed": [], "status": "started"})
        assert all("Step" in step for step in result["steps_completed"])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
