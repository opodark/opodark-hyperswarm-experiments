import json
import os
import time
import requests
from datetime import datetime

# ─────────────────────────────
# CONFIG
# ─────────────────────────────

REGISTRY_PATH = "/var/lib/hyperswarm/registry.json"

GOSSIP_INTERVAL = 15  # seconds

KNOWN_PEERS = [
    "http://192.168.1.101:8000",
    "http://192.168.1.102:8000"
]


# ─────────────────────────────
# LOCAL REGISTRY
# ─────────────────────────────

def _ensure_path():

    os.makedirs(os.path.dirname(REGISTRY_PATH), exist_ok=True)


def load_registry():

    if not os.path.exists(REGISTRY_PATH):

        return {"nodes": {}, "updated_at": None}

    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)


def save_registry(data):

    _ensure_path()

    data["updated_at"] = datetime.utcnow().isoformat()

    with open(REGISTRY_PATH, "w") as f:
        json.dump(data, f, indent=2)


# ─────────────────────────────
# MERGE LOGIC (SEMPLICE MVP)
# ─────────────────────────────

def merge(local, remote):

    local_nodes = local.get("nodes", {})
    remote_nodes = remote.get("nodes", {})

    for node_id, node_data in remote_nodes.items():

        if node_id not in local_nodes:

            local_nodes[node_id] = node_data
            continue

        # last write wins (MVP)
        if node_data.get("last_seen", "") > local_nodes[node_id].get("last_seen", ""):

            local_nodes[node_id] = node_data

    local["nodes"] = local_nodes

    return local


# ─────────────────────────────
# FETCH FROM PEER
# ─────────────────────────────

def fetch_peer(peer_url):

    try:

        r = requests.get(f"{peer_url}/registry", timeout=3)

        return r.json()

    except Exception:

        return None


# ─────────────────────────────
# GOSSIP CYCLE
# ─────────────────────────────

def gossip_loop():

    while True:

        local = load_registry()

        for peer in KNOWN_PEERS:

            remote = fetch_peer(peer)

            if not remote:
                continue

            local = merge(local, remote)

        save_registry(local)

        print("[GOSSIP] sync complete:", len(local.get("nodes", {})))

        time.sleep(GOSSIP_INTERVAL)