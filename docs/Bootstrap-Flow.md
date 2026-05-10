# Bootstrap Flow

## Sequenza base

1. Il nodo genera o recupera `node_id`.
2. Il nodo carica il proprio state locale.
3. Il nodo si registra al bootstrap server.
4. Il bootstrap server lo marca online.
5. Il nodo invia heartbeat periodici.

## Comportamento idempotente

Se il nodo è già provisioned:
- non ripete il deploy,
- entra direttamente in heartbeat loop,
- continua a segnalare presenza al control plane.

## Obiettivo

Il bootstrap deve essere ripetibile e prevedibile.