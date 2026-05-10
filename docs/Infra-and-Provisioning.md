# Infra and Provisioning

## Scopo

L’infra serve a generare e ripetere ambienti uguali per:
- VM,
- bare metal,
- container,
- bootstrap locale.

## Strumenti

- `cloud-init`
- `Ansible`
- `PXE`
- `Docker Compose`

## Principio

Ogni deployment deve essere ricreabile da zero con pochi file e comandi.

## Template

I template vanno tenuti nella cartella `authority/templates/` e usati dal backend per generare output specifici per il metodo di boot.