from datetime import datetime, timezone
import os

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["VERSION"] = os.getenv("APP_VERSION", "0.1.0")

    @app.get("/")
    def home():
        return jsonify(
            message="Hello from the DevOps learning app!",
            service="devops-demo",
            version=app.config["VERSION"],
        )

    @app.get("/health")
    def health():
        """A lightweight liveness endpoint for a load balancer or orchestrator."""
        return jsonify(status="ok", timestamp=datetime.now(timezone.utc).isoformat())

    @app.get("/ready")
    def ready():
        """A readiness endpoint; extend this when adding dependencies such as a database."""
        return jsonify(status="ready")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
