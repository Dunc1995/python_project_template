import pytest
from package import app, models

def test_answer():
    assert app.main() == 'Hello World!'