# Logging

Python has built-in logging module that can be used for basic logging.

The [documentation](https://docs.python.org/3/howto/logging.html)

## Example using logging

## [Loggin levels](https://docs.python.org/3/library/logging.html?highlight=logging#logging-levels)

Level Value
CRITICAL: 50
ERROR: 40
WARNING: 30
INFO: 20
DEBUG: 10
NOTSET 0

## Configuration

The configuration is done using method basicConfig

```python
"""
Define loggin with file and format
2020-04-28 16:22|root|INFO|divide 10 by 345
"""
logging.basicConfig(filename=file,
  level=logging.INFO,
  format="%(asctime)s|%(name)s|%(levelname)s|%(message)s",
  datefmt="%Y-%m-%d %H:%M")

```

Excellent tutorial about class logging [is here](https://www.youtube.com/watch?v=jxmzY9soFXg)

## Alternatives

There are open source alternatives for specific usecases. [Sentry](https://docs.sentry.io/server/installation/) is open source alternative. It is quite easy to integrate into Front-end or backend parts of the code.
