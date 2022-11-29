from flaska import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_which_always_fail(client):
    response = client.get("/hello")
    assert response.status_code == 200