
from web import app
from unittest import mock
from base64 import b64encode
# from pytest import

client = app.test_client()

def test_homepage():
  resp = client.get("/")
  assert resp.status_code == 200


auth={
  "authorization":{
    "password":"password"
  }
}

def test_login_ok():
  cred = b64encode(b"test_user:password").decode('utf-8')
  headers={
    "Authorization": f"Basic {cred}"
  }
  resp = client.get("/login",headers=headers)
  assert resp.status_code == 200


def test_login_failed():
  cred = b64encode(b"test_user:wrong_password").decode('utf-8')
  headers={
    "Authorization": f"Basic {cred}"
  }
  resp = client.get("/login",headers=headers)
  assert resp.status_code == 401


@mock.patch('web.routes.jwt')
def test_login_jwt(jwt):
  cred = b64encode(b"test_user:password").decode('utf-8')
  headers={
    "Authorization": f"Basic {cred}"
  }
  resp = client.get("/login",headers=headers)
  jwt.encode.assert_called_once()

@mock.patch('web.routes.jwt.encode')
def test_login_jwt_jsonify(encode):
  # note the order is bottom-up
  cred = b64encode(b"test_user:password").decode('utf-8')
  headers={
    "Authorization": f"Basic {cred}"
  }
  resp = client.get("/login",headers=headers)
  #jwt.encode.assert_called_once()
  fake_token = bytes("FAKE_TOKEN",'UTF-8')
  # jwt.encode = mock()
  encode.return_value = fake_token
  # jwt.encode.return_value="FAKE_TOKEN"
  # jsonify.assert_called_once_with({"token":"FAKE_TOKEN"})
  encode.assert_called_once()
  # assert resp.status_code == 200


def test_protected_missing_token():
  resp = client.get("/protected")
  assert resp.get_json() ==  {"message":"Token is missing"}
  assert resp.status_code == 401


def test_protected_invalid_token():
  resp = client.get("/protected?token=123454")
  assert resp.get_json() ==  {'message':'Token is NOT VALID!'}
  assert resp.status_code == 403