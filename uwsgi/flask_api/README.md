# uWSGI setup

```bash
# load env
source env/bin/activate
# install
pip install wheel uwsgi flask
# save as requirements
pip freeze > requirements.txt
```

## uWSGI ini file

The setup is based on [this document](https://pythonise.com/series/learning-flask/building-a-flask-app-with-docker-compose).

In addition, more info can be found in [this document](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04).

## Dockerfile

```bash
# build flask api container
docker build . --tag=food_flask_api
# test run container
docker run -it -p 5001:5001 food_flask_api
```
