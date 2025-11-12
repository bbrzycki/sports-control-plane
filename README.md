# sports-control-plane

Service layer that surfaces forecasts, backtests, and orchestration status from the sports data platform.

## Goals

- REST + WebSocket API for dashboards, MCP server, and automation tools.
- Daily digest summarising model performance and proposed wagers (integrates with betpy registries).
- Hooks for model promotion (MLflow), DAG triggers (Airflow), and alerting.

## Planned structure

```
app/
  api/          # FastAPI routers (forecasts, runs, auth)
  services/     # Clients for warehouse, MLflow, Airflow
  deps.py       # Dependency injection wiring
ui/
  dashboard/    # Streamlit or Next.js front-end
infra/
  terraform/    # Infrastructure as code for cloud deployment
config/
  dev.yaml
  staging.yaml
```

Implementation will start after the core data platform and bet utilities are stabilised.

## Docker quick start

```bash
docker network create sports_net  # one-time shared network
docker compose up --build
```

The service listens on `http://localhost:9000/healthz` by default.
