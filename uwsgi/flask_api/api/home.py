from flask import request
from api import app

@app.route("/",methods=["GET"])
def home():
  return {
    'status':200,
    'statusText':"OK",
    'data':{
      'message':'Welkom to Flask test api. Everything works FINE!'
    }
  }

@app.route("/api",methods=["GET"])
def apiHome():
  return {
    'status':200,
    'statusText':"OK",
    'data':{
      'message':'Welkom to Flask test api. This is /api POINT'
    }
  }

@app.route("/l2",methods=["GET","POST"])
def l2api():
  if request.method=="GET":
    return {
      'status':200,
      'statusText':"OK",
      'data':{
        'message':'Welkom to Flask test api. This is /l2 POINT'
      }
    }
  if request.method=="POST":
    return {
      'status':200,
      'statusText':"OK",
      'data': request.json
    }

@app.route("/l2/<id>",methods=["GET"])
def idl2api(id):
  return {
    'status':200,
    'statusText':"OK",
    'data':{
      'message': f'Welkom to Flask test api. This is /l2 POINT FOR id:{id}'
    }
  }