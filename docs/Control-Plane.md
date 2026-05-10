# Control Plane

Il control plane è la coordinazione runtime dello swarm.

## Responsabilità

- Registry dei nodi.
- Task management.
- Event streaming.
- Dispatch dei task.
- Stato operativo minimo.

## Non responsabilità

- Non deve diventare il collo di bottiglia dell’inferenza.
- Non deve contenere tutta la logica di deploy.
- Non deve sostituire l’autorità del team.

## Stato attuale

La versione experimental è il posto giusto dove testare il flusso control plane prima del merge nel repo principale.