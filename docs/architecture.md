# Architecture

HyperSwarm segue una logica a strati.

## 1. Bootstrap

Il bootstrap si occupa di generare o recuperare un node ID, registrare il nodo e mantenere il heartbeat vivo.

## 2. Control Plane

Il control plane gestisce registry, task, events, state e scheduling minimo.

## 3. Authority

L’authority è il livello team-facing: deploy wizard, template rendering, token di join, policy e onboarding.

## 4. Agent Runtime

L’agent esegue task locali, contatta Ollama e restituisce il risultato al control plane.

## 5. Infra

L’infra genera ambienti ripetibili con cloud-init, PXE, Ansible e Docker Compose.

## Nota di design

Il centrale deve coordinare, non monopolizzare l’intelligenza.