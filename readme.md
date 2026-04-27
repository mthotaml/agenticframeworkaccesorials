# Accessorial Recommendation Agent POC

## Overview
This POC demonstrates an AI-powered system that recommends shipment accessorials
based on operational signals.

## Features
- Accessorial recommendations
- Confidence scoring
- Explanation + evidence
- Latency tracking
- Kill switch support
- Evaluation metrics

## Run Instructions

```bash
pip install -r requirements.txt
uvicorn app:app --reload --port 8000

Open:
http://localhost:8000
API
POST /api/recommend
Example Input:
{
"shipment_mode": "LTL",
"location_type": "hospital",
"has_loading_dock": false,
"has_forklift": false
}
Evaluation
GET /api/evaluate
Returns:
Precision
Recall
F1 Score
Guardrails
Kill switch via environment variable
Confidence-based rollout
Closed set of accessorials (no hallucination)
Tradeoffs
Rules-based model for explainability
Prioritized precision over recall
Lightweight for low latency
