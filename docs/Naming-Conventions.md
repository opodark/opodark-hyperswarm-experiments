# Naming Conventions

## Python

- Usa `snake_case`.
- Usa `control_plane` come package importabile.
- Non usare trattini nei package Python.

## Docker

- Usa nomi leggibili per servizi e container.
- `control-plane` va bene per visibilità umana in compose.
- I mount filesystem devono riflettere la cartella reale.

## Docs

- Usa `control plane` nel testo normale.
- Usa `control_plane` solo quando ti riferisci al codice.

## Esempi

- Corretto: `from control_plane.core.state import init_state`
- Corretto: `../../control_plane/api:/app`
- Corretto: `hyperswarm-control-plane`
- Non corretto: package Python con `-`.