# DevOps Learning App

A deliberately small Flask API for practicing the DevOps lifecycle.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt pytest
pytest -q
python app.py
```

Visit `http://localhost:5000/`, then check `http://localhost:5000/health` and `http://localhost:5000/ready`.

## Run with Docker

```powershell
docker build -t devops-demo:local .
docker run --rm -p 5000:5000 -e APP_VERSION=local devops-demo:local
```

## DevOps exercises

1. Push the project to GitHub and watch the CI workflow run.
2. Publish the Docker image to a registry.
3. Add a Kubernetes deployment that probes `/health` and `/ready`.
4. Add structured logs, metrics, and a real dependency to evolve the readiness check.
