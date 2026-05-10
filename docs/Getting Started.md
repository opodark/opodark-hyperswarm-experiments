# Getting Started

Questa pagina spiega come entrare nel progetto senza rompere nulla.

## Prerequisiti

- Git.
- Python 3.11+.
- Docker e Docker Compose.
- Conoscenza base di FastAPI e shell Unix.

## Flusso consigliato

1. Clona la repo experimental.
2. Crea un branch dedicato.
3. Lavora solo lì.
4. Fai test e commit piccoli.
5. Push frequente.

## Comandi base

```bash
git clone https://github.com/opodark/opodark-hyperswarm-experiments.git hyperswarm-experimental
cd hyperswarm-experimental
git switch -c feature/<nome>
```

## Check iniziali

```bash
git status
git remote -v
git branch
```

## Regola fondamentale

Prima di rinominare cartelle o package, verifica sempre i riferimenti con `grep -R`.