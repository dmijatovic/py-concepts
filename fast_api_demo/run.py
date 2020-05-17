import uvicorn
from website import config

if __name__== "__main__":
  uvicorn.run("website:app",\
    host='0.0.0.0',\
    port=int(config.PORT),\
    reload=True,\
    debug=True,\
    workers=1)