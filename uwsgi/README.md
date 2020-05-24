# Production setup for Flask apps

This is demo for basic uWSGI webapp using NGINX and Flask. There are different approaches: there are readily avaliable images.

This [video demos](https://www.youtube.com/watch?v=dVEjSmKFUVI) one of the very basis approaches.

NGINX support uWSGI natively. [See documentation](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html).

In this demo we try to create basic docker-compose setup based on the above video learnings but from basic python3.7 and nginx images avaliable on Docker.

## Remarks

NGINX url rewrite is not working properly. The request send to nginx/api should be send to flask_api without /api in the url. For example /api should be only /
