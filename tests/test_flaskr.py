import os

import pytest

from flask import Flask


@pytest.fixture
def client():
    _app = Flask(__name__)

    with _app.test_client() as client:
        yield client

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'was not found on the server' in rv.data
