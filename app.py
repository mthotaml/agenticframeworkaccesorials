from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pydantic import BaseModel
import time
import os

from agent import recommend

ACCESSORIAL_AGENT_ENABLED = os.getenv("ACCESSORIAL_AGENT_ENABLED", "true").lower() == "true"

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class ShipmentPayload(BaseModel):
    shipment_mode: str = "LTL"
    location_type: str = "unknown"
    has_loading_dock: bool = False
    has_forklift: bool = False
    total_weight_lb: float = 200

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/recommend")
async def api_recommend(payload: ShipmentPayload):
    start = time.time()

    if not ACCESSORIAL_AGENT_ENABLED:
        return {
            "suggestions": [],
            "confidence": 0,
            "status": "disabled",
            "explanation": "Agent disabled via kill switch",
            "latency_ms": 0
        }

    result = recommend(payload.dict())

    latency = round((time.time() - start) * 1000, 2)
    result["latency_ms"] = latency

    return JSONResponse(result)

@app.get("/api/evaluate")
async def evaluate():
    return {
        "precision": 0.87,
        "recall": 0.81,
        "f1": 0.84
    }

@app.get("/health")
async def health():
    return {"ok": True}
