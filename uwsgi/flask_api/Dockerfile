FROM python:3.6

# open /api
WORKDIR /home/flask_api

# copy current directory to /api
COPY . /home/flask_api

# install deps
RUN pip install -r requirements.txt

EXPOSE 5001
EXPOSE 5002

# run the command to start uWSGI
CMD ["uwsgi", "uwsgi.ini"]
