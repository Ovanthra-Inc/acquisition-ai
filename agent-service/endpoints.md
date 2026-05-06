# Agent Service Endpoints

## Core Endpoints
- `POST /api/v1/agent/run` - Runs an agent workflow for a given goal
- `GET /api/v1/agent/{task_id}` - Gets status of an agent task
- `POST /api/v1/agent/{task_id}/pause` - Pauses an agent task
- `POST /api/v1/agent/{task_id}/resume` - Resumes a paused agent task
- `POST /api/v1/agent/{task_id}/cancel` - Cancels an agent task
- `GET /api/v1/agent/{task_id}/steps` - Lists execution steps of an agent task
