import pytest
from flaska.db import get_db


def test_index(client, auth):
    response = client.get("/auth/login")
    assert b"Log In" in response.data
    assert b"Register" in response.data

    auth.login()
    response = client.get("/")
    assert b"Log Out" in response.data
    assert b"Flask App" in response.data