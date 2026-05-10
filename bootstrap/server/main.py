from fastapi import FastAPI
from datetime import datetime, timedelta
from typing import Dict

app = FastAPI(title="HyperSwarm Bootstrap Server")

# ─────────────────────────────
# NODE REGISTRY (in-memory MVP)
# ─────────────────────────────

NODES: Dict[str, dict] = {}

HEARTBEAT_TIMEOUT_SECONDS = 30


# ─────────────────────────────
# REGISTER NODE
# ─────────────────────────────

@app.post("/register")
def register(node: dict):

    node_id = node.get("node_id")

    if not node_id:
        return {"error": "missing node_id"}

    node["last_seen"] = datetime.utcnow().isoformat()
    node["status"] = "online"

    NODES[node_id] = node

    return {
        "status": "registered",
        "node_id": node_id
    }


# ─────────────────────────────
# HEARTBEAT
# ─────────────────────────────

@app.post("/heartbeat")
def heartbeat(payload: dict):

    node_id = payload.get("node_id")

    if node_id not in NODES:
        return {"error": "node not registered"}

    NODES[node_id]["last_seen"] = datetime.utcnow().isoformat()
    NODES[node_id]["status"] = "online"

    return {"status": "ok"}


# ─────────────────────────────
# GET ALL NODES
# ─────────────────────────────

@app.get("/nodes")
def get_nodes():

    now = datetime.utcnow()

    updated = {}

    for node_id, node in NODES.items():

        last_seen = datetime.fromisoformat(node["last_seen"])

        delta = now - last_seen

        if delta > timedelta(seconds=HEARTBEAT_TIMEOUT_SECONDS):
            node["status"] = "stale"
        else:
            node["status"] = "online"

        updated[node_id] = node

    return updated


# ─────────────────────────────
# HEALTH CHECK
# ─────────────────────────────

@app.get("/")
def root():

    return {
        "service": "hyperswarm-bootstrap",
        "nodes": len(NODES)
    }