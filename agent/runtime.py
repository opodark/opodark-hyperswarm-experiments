import time
import requests

OLLAMA_URL = "http://localhost:11434"

def ask_model(prompt):

    return requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    ).json()["response"]


while True:

    result = ask_model("You are a swarm node. Say status.")

    print(result)

    time.sleep(30)