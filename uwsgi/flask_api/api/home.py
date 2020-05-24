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