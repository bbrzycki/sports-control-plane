"""FastAPI app providing endpoints for control-plane interactions."""
from __future__ import annotations

from fastapi import FastAPI

app = FastAPI(title="Sports Control Plane")


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
