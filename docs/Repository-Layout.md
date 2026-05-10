# Repository Layout

## Struttura attuale

- `bootstrap/`: bootstrap server e client.
- `control_plane/`: API, state, registry, scheduler, memory e models.
- `authority/`: wizard, deploy templates, team management e RBAC.
- `frontend/`: interfacce utente e stack Open WebUI.
- `infra/`: cloud-init, Ansible, PXE, Docker e provisioning.
- `docs/`: documentazione architetturale e operativa.

## Regola di naming

- `control_plane` per package Python e path filesystem.
- `control-plane` solo se serve leggibilità nei nomi Docker/compose.
- `control plane` nel testo umano.

## File generati

Dump, cache e file temporanei non devono finire in Git.