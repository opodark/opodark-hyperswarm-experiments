import socket
import uuid
import requests

BOOTSTRAP_SERVER = "http://localhost:9000"

node = {

    "node_id": str(uuid.uuid4()),

    "hostname": socket.gethostname(),

    "role": "research",

    "model": "deepseek-r1:7b"
}

requests.post(
    f"{BOOTSTRAP_SERVER}/register",
    json=node
)