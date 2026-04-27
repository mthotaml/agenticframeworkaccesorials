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
