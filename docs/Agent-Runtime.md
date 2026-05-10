# Agent Runtime

L’agent è il worker locale del nodo.

## Responsabilità

- Poll dei task.
- Esecuzione locale.
- Chiamate a Ollama.
- Retry su errori transitori.
- Report del risultato al control plane.

## Regole

- Task validity prima dell’esecuzione.
- Logging chiaro.
- Nessun blocco totale su singolo task fallito.
- Heartbeat separato dall’esecuzione.

## Obiettivo

Trasformare ogni nodo in un worker robusto e ripetibile.