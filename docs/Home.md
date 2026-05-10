# HyperSwarm Wiki

HyperSwarm è una piattaforma di AI distribuita per orchestrare agenti locali, bootstrap automatico dei nodi, control plane centrale e osservabilità.

Questo wiki serve a:
- allineare il team sul linguaggio del progetto,
- documentare la struttura tecnica,
- definire le regole di contribuzione,
- ridurre ambiguità su naming, routing e responsabilità dei moduli.

## Principi guida

- Distribuzione prima di centralizzazione.
- Bootstrap ripetibile.
- Naming coerente.
- Repo pulita.
- Modifiche piccole e verificabili.

## Componenti principali

- `bootstrap/`: registrazione nodi e heartbeat.
- `control_plane/`: registry, task, state, scheduling.
- `authority/`: wizard deploy, policy, template rendering.
- `frontend/`: UI e stack Open WebUI.
- `infra/`: cloud-init, Ansible, PXE, Docker.
- `docs/`: architettura e note operative.

## Stato attuale

La repo experimental è il terreno di prova per:
- authority centrale,
- wizard di deploy,
- control plane modulare,
- validazione del bootstrap client,
- cleanup del naming e delle dipendenze.

## Dove iniziare

Vai alla pagina [[Getting Started]].