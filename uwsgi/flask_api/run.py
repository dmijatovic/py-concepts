import os

from api import app

API_PORT = os.environ.get("API_PORT", 5001)

if __name__=="__main__":
  app.run(debug=True, host="0.0.0.0", port=API_PORT)