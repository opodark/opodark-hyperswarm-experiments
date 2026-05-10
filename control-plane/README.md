# HyperSwarm Control Plane

The Control Plane is the central coordination layer of HyperSwarm.

It is responsible for:

- Node registry (laptop agents)
- Task management (Jira-like system)
- Event streaming (observability layer)
- Swarm coordination logic

## Architecture

The system exposes:

- REST API (FastAPI)
- CLI tool (swarmctl)
- In-memory state (MVP)
- Future: persistent DB + event store

## Components

- API → manages nodes, tasks, events
- CLI → operator interface
- Core → scheduling logic (future evolution)

## Goal

Make the entire swarm behave like a single organism.

## memo:

uvicorn main:app --reload --port 8000