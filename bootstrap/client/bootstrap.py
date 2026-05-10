import uuid
import socket
import requests

BOOTSTRAP_SERVER = "http://192.168.1.10:9000"

node = {

    "node_id": str(uuid.uuid4()),

    "hostname": socket.gethostname(),

    "ip": socket.gethostbyname(socket.gethostname()),

    "role": "auto",

    "model": "phi3:mini",

    "capabilities": [
        "ollama",
        "cpu",
        "vulkan"
    ]
}

try:

    r = requests.post(
        f"{BOOTSTRAP_SERVER}/register",
        json=node,
        timeout=5
    )

    print("REGISTERED:", r.json())

except Exception as e:

    print("BOOTSTRAP ERROR:", e)