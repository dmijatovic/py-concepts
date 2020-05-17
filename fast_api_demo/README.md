# FastAPI

This is new modern REST API centric web server for python.

Additional packages used

- jinja2: templating engine used by flask too
- aiofiles: serving static content
- uvicorn: webserver with multiple workers to spread the load

```bash
# install all dependencies
pip install fastapi jinja2 aiofiles uvicorn
```

The tutorials used to learn FastAPI

- https://github.com/perfecto25/sparky

## Errors

When installing uvicorn I got an error:

```bash
uvloop/loop.c:20:10: fatal error: Python.h: No such file or directory
  #include "Python.h"
```

It seems I needed to install python dev headers library.

```bash
# installed the header files and static libraries for python dev
sudo apt-get install python3-dev
```

## Swagger docs

FastAPI generates swagger documentation from your doc strings. The documentation is avaliable at /docs route of the api.
