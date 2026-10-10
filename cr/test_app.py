from app import create_app


def test_home_returns_service_details():
    client = create_app().test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["service"] == "devops-demo"


def test_health_check_is_ok():
    client = create_app().test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_ready_check_is_ready():
    client = create_app().test_client()
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json == {"status": "ready"}
