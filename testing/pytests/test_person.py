import pytest
from unittest import mock
from person import greet, attack_damage

# ------------------------------------
# Create fixture values to test method
# ------------------------------------
@pytest.fixture
def person():
  return {"name":"Dusan"}

def test_greet(person):
  assert greet(person) == "Hello Dusan"


#------------------------------------
# Mock system methods
#------------------------------------
# parameters (module.method, value to return from mock, check for parameters count)
@mock.patch("person.randint",return_value=10,autospec=True)
def test_attack_damage(mock_randint):
  assert attack_damage(1) == 10
