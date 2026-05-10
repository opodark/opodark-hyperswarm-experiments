import json
import os
from datetime import datetime

STATE_PATH = "/etc/hyperswarm/state.json"
DEPLOY_FLAG = "/etc/hyperswarm/.deploy"

DEFAULT_STATE = {
    "node_id": None,
    "role": "auto",
    "model": "phi3:mini",
    "provisioned": False,
    "version": "0.1",
    "created_at": None,
    "last_boot": None
}

def _ensure_dir():
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)

def _load_raw():
    if not os.path.exists(STATE_PATH):
        return None
    with open(STATE_PATH, "r") as f:
        return json.load(f)

def _save_raw(state: dict):
    _ensure_dir()
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def get_state():
    state = _load_raw()
    if state is None:
        return DEFAULT_STATE.copy()
    return state

def init_state(node_id: str, role: str = "auto", model: str = "phi3:mini"):
    state = get_state()
    if state.get("node_id"):
        return state
    state.update({
        "node_id": node_id,
        "role": role,
        "model": model,
        "provisioned": False,
        "created_at": datetime.utcnow().isoformat(),
        "last_boot": datetime.utcnow().isoformat()
    })
    _save_raw(state)
    return state

def mark_provisioned():
    state = get_state()
    state["provisioned"] = True
    state["last_boot"] = datetime.utcnow().isoformat()
    _save_raw(state)
    _ensure_dir()
    with open(DEPLOY_FLAG, "w") as f:
        f.write("provisioned")

def is_provisioned():
    return os.path.exists(DEPLOY_FLAG)

def update_state(updates: dict):
    state = get_state()
    state.update(updates)
    state["last_boot"] = datetime.utcnow().isoformat()
    _save_raw(state)
    return state

def reset_state():
    if os.path.exists(STATE_PATH):
        os.remove(STATE_PATH)
    if os.path.exists(DEPLOY_FLAG):
        os.remove(DEPLOY_FLAG)
