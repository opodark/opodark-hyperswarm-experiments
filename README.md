# HyperSwarm

Distributed AI swarm platform with:

- multi-agent orchestration
- shared semantic memory
- observability
- task execution
- PXE auto-join infrastructure

🧾 CHANGELOG — HyperSwarm Update
🚀 Agent Runtime V2 (stability upgrade)
✨ Added
Introduced task queue (deque buffer) for safer task handling
Added retry mechanism with exponential backoff
Implemented structured logging system (INFO/WARN/ERROR)
Added task validation layer (assigned + node match)
Separated execution pipeline:
fetch → queue → process → execute → report
🔁 Improved
Ollama calls now wrapped with timeout + error handling
Control plane requests hardened with try/except + logging
Task execution flow now resilient to transient failures
🧠 Reliability upgrades
Agent no longer blocks on single task failure
Failed LLM calls automatically retried (up to 3 attempts)
Permanent failure handling with explicit error reporting
Queue-based processing prevents task loss during fetch cycles
🧹 Refactored
Clean separation of responsibilities:
fetch_tasks()
update_queue()
process_task()
execute_with_retry()
Removed implicit inline execution loop
Structured main loop for predictable runtime behavior
📡 System impact
Agent runtime is now production-stable worker model
Enables safe scaling to multiple nodes
Prepares foundation for:
distributed scheduling
memory injection layer
observability integration
🧭 Next steps (planned)
Streaming LLM responses (token-level logs)
Memory (MSA integration)
Smart dispatch scoring in control plane
Gossip registry sync between nodes


er Manifesto! ....------>

# ◈ HYPERSWARM

> *"The network is the mind. The node is the self. The swarm is the revolution."*

---

## Manifesto

Ogni sistema centralizzato è un punto di controllo.  
Ogni punto di controllo è una catena.  
Ogni catena può essere spezzata.

**HyperSwarm** nasce da una convinzione semplice e radicale:  
l'intelligenza artificiale non dovrebbe appartenere a nessun server, nessun cloud, nessuna entità.  
Dovrebbe essere *distribuita come il pensiero umano* — ovunque e in nessun posto.

Non esiste un coordinatore centrale.  
Non esiste un punto di fallimento unico.  
Non esiste un padrone della rete.

Esiste solo lo sciame.

---

## Architettura

HyperSwarm opera su una topologia **ibrida** — parte mesh peer-to-peer, parte rete classica client-server — perché il mondo reale non è mai puramente uno dei due.

```
                    ╔══════════════════════════════╗
                    ║       HYPERSWARM FABRIC       ║
                    ╚══════════════════════════════╝

  ┌─────────┐   mesh   ┌─────────┐   mesh   ┌─────────┐
  │ NODE  A │ ◄──────► │ NODE  B │ ◄──────► │ NODE  C │
  │  Ollama │          │  Ollama │          │  Ollama │
  └────┬────┘          └────┬────┘          └────┬────┘
       │  \                 │                /   │
       │   \___________     │    ___________/    │
       │               ↓   ↓   ↓                │
       │           ┌──────────────┐              │
       │           │  ORCHESTRATOR│              │
       │           │  (bootstrap) │              │
       │           └──────┬───────┘              │
       │                  │ classic              │
       └──────────────────┤ network  ────────────┘
                          │
                   ┌──────┴───────┐
                   │ SHARED MEMORY│
                   │  (vector db) │
                   └──────────────┘
```

### Layer mesh (P2P)

I nodi si trovano, si autoscoprono, si connettono.  
Nessun registro. Nessuna autorità di certificazione.  
Il bootstrap avviene via **PXE auto-join**: accendi un nodo sulla rete locale, e lo sciame lo assorbe.  
Il heartbeat è il respiro del sistema — silenzioso, continuo, vitale.

### Layer classico (orchestrazione)

Esiste un orchestratore — ma è *funzionale*, non *feudale*.  
Coordina i task, smista il lavoro, mantiene l'osservabilità.  
Può essere sostituito, replicato, rimosso.  
Non è il re. È il postino.

### Memoria condivisa

Ogni agente vive nel presente.  
La memoria vettoriale è il passato condiviso dello sciame —  
un substrato semantico dove i contesti persistono,  
dove un nodo può ricordare ciò che un altro ha imparato.  
Distribuita. Interrogabile. Libera.

---

## Principi

**I. Nessun Single Point of Failure**  
Se un nodo muore, lo sciame continua. Sempre.

**II. Inferenza locale, prima di tutto**  
Ogni nodo gira Ollama in locale. Nessun dato esce dalla rete senza consenso esplicito.  
Il modello è tuo. Il peso è tuo. Il pensiero è tuo.

**III. Osservabilità totale, controllo distribuito**  
Tutto viene tracciato — eventi, latenze, ragionamenti —  
ma nessun singolo operatore detiene il pannello di controllo supremo.  
La trasparenza è un diritto, non un privilegio.

**IV. L'infrastruttura è codice, il codice è politica**  
Un `docker-compose.yml` è una dichiarazione di intenti.  
Un PXE boot è un atto di sovranità computazionale.  
Ogni commit in questo repository è un voto per un futuro diverso.

**V. La rete non chiede il permesso**  
I nodi si uniscono allo sciame perché *scelgono* di farlo.  
Nessuna registrazione. Nessun account. Nessun ToS.  
Solo chiavi, protocolli, e la fisica dei pacchetti.

---

## Stack

| Componente | Tecnologia | Ruolo |
|---|---|---|
| Agent runtime | Ollama (Python) | Cervello di ogni nodo |
| Orchestratore | FastAPI + task queue | Coordinamento funzionale |
| Memoria | ChromaDB / Qdrant | Contesto semantico condiviso |
| Bootstrap | PXE + heartbeat | Auto-scoperta nella rete locale |
| Osservabilità | Event stream + traces | Visibilità senza centralizzazione |
| Frontend | Open WebUI / LibreChat | Interfaccia umana opzionale |
| Infra | Docker Compose | Deployment riproducibile |

---

## Struttura del repository

```
hyperswarm/
├── agent/          # Runtime agenti — il cuore pulsante
├── bootstrap/      # Auto-join e heartbeat — il sistema nervoso
├── infra/          # Deployment e configurazione
├── observability/  # Tracciamento eventi e metriche
├── docs/           # Documentazione
└── docker-compose.yml
```

### In costruzione

```
hyperswarm/
├── backend/        # Orchestratore + sistema task         [TODO]
├── memory/         # Memoria vettoriale condivisa         [TODO]
└── frontend/       # Integrazione Open WebUI / LibreChat  [TODO]
```

---

## Avvio rapido

```bash
# Clona lo sciame
git clone https://github.com/opodark/hyperswarm.git
cd hyperswarm

# Avvia il cluster locale
docker compose up -d

# Un nodo si unisce automaticamente via bootstrap
# Nessuna configurazione manuale richiesta
```

Il sistema si auto-organizza.  
Questo è il punto.

---

## Roadmap

Lo sciame cresce per strati, non per decisioni di comitato.

- [x] Struttura base del progetto
- [x] Bootstrap e auto-join PXE
- [x] Osservabilità (event stream, traces, logs)
- [x] Infrastruttura Docker
- [ ] Orchestratore backend + sistema task
- [ ] Memoria vettoriale condivisa
- [ ] Integrazione frontend (Open WebUI / LibreChat)
- [ ] Federation inter-sciame (sciami di sciami)
- [ ] Crittografia end-to-end tra nodi

---

## Contribuire

Non si chiede il permesso per contribuire a una rete libera.

```bash
git fork
git branch feature/il-tuo-contributo
git commit -m "aggiungo libertà al sistema"
git push
```

Apri una pull request. Discuti. Migliora.  
Il codice è comune. Il progresso è collettivo.

---

## Licenza

MIT — perché il software libero non è un favore,  
è un prerequisito della civiltà digitale.

---

```
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
  ░  "Don't trust. Verify. Then distribute." ░
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

*HyperSwarm — Distributed AI for a decentralized world.*