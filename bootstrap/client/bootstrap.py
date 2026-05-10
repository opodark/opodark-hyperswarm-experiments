import uuid
import socket
import requests
import time
import os

from control_plane.core.state import (
    init_state,
    is_provisioned,
    mark_provisioned
)

BOOTSTRAP_SERVER = "http://192.168.1.10:9000"
STATE_NODE_ID_PATH = "/etc/hyperswarm/node_id"

def get_or_create_node_id():
    os.makedirs("/etc/hyperswarm", exist_ok=True)

    if os.path.exists(STATE_NODE_ID_PATH):
        with open(STATE_NODE_ID_PATH, "r") as f:
            return f.read().strip()

    node_id = str(uuid.uuid4())

    with open(STATE_NODE_ID_PATH, "w") as f:
        f.write(node_id)

    return node_id

def build_node(node_id):
    return {
        "node_id": node_id,
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "role": "auto",
        "model": "phi3:mini",
        "capabilities": [
            "ollama",
            "cpu"
        ]
    }

def register(node):
    try:
        r = requests.post(
            f"{BOOTSTRAP_SERVER}/register",
            json=node,
            timeout=5
        )
        print("[BOOTSTRAP] registered:", r.json())
        return True
    except Exception as e:
        print("[BOOTSTRAP ERROR]", e)
        return False

def heartbeat(node_id):
    while True:
        try:
            requests.post(
                f"{BOOTSTRAP_SERVER}/heartbeat",
                json={"node_id": node_id},
                timeout=5
            )
            print("[HEARTBEAT] ok")
        except Exception as e:
            print("[HEARTBEAT ERROR]", e)

        time.sleep(10)

def main():
    node_id = get_or_create_node_id()

    init_state(node_id=node_id)

    if is_provisioned():
        print("[BOOTSTRAP] already provisioned, skipping deploy")
        heartbeat(node_id)
        return

    node = build_node(node_id)
    ok = register(node)

    if not ok:
        print("[BOOTSTRAP] failed registration, retrying loop")
        heartbeat(node_id)
        return

    mark_provisioned()
    print("[BOOTSTRAP] provisioning complete")
    heartbeat(node_id)

if __name__ == "__main__":
    main()
