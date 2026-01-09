# Example 08: Multi-Step Workflow

## Overview
Sequential data processing pipeline with multiple stages.

## What to Do
Execute a 4-step workflow: collect → validate → process → save

## Inputs
- Trigger button to start workflow
- No additional inputs required

## Expected Outputs
- **Steps Completed**: List of 4 completed steps
- **Status**: "completed" after all steps
- Each step logs its completion

## Graph Structure
```
START → collect → validate → process → save → END
```

## State Schema
```python
{
    "data": dict,
    "steps_completed": list,
    "status": str
}
```

## Learning Objectives
- Multi-step sequential processing
- Workflow orchestration
- Step tracking
- Status management
