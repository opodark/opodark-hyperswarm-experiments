from fastapi import FastAPI

app = FastAPI()

NODES = {}

@app.get("/")
def root():

    return {
        "service": "hyperswarm-bootstrap",
        "nodes": len(NODES)
    }

@app.post("/register")
def register(node: dict):

    NODES[node["node_id"]] = node

    return {
        "status": "registered"
    }