# Authority

L’authority è il livello centrale per il team.

## Responsabilità

- Team management.
- RBAC.
- Registry nodi.
- Wizard deploy.
- Token di join.
- Rendering manifest.
- Policy di onboarding.

## Idee chiave

- Il wizard non installa a mano: genera un deployment spec.
- Il backend traduce il wizard in cloud-init, Ansible, Compose o config agent.
- La UI deve restare semplice finché il motore non è stabile.

## Stato MVP

Per ora bastano:
- API FastAPI,
- modelli Pydantic,
- servizi per token e rendering,
- template Jinja2.