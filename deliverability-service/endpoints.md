# Deliverability Service Endpoints

## Core Endpoints
- `GET /api/v1/deliverability/domains` - List domains with reputation metadata (not yet fully implemented)
- `POST /api/v1/deliverability/warmup` - Initiate domain warmup processes
- `GET /api/v1/deliverability/reputation` - Fetch reputation scores for tracking
- `POST /api/v1/deliverability/reputation/calculate` - Recalculate reputation based on bounce/spam metrics
