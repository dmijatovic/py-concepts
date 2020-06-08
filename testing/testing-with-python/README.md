# Testing python with pytest

Software testing and testing automation with Python short-course.

This course is based on [the video](https://www.youtube.com/watch?v=LX2ksGYXJ80&list=PLRiZb4DNOVQeSqmV21DErxbP8HqgGari2&index=13)

And the repo is [cloned from here](https://github.com/LeemanGeophysicalLLC/testing-with-python)

The training material is [avaliable here](https://leemangeophysicalllc.github.io/testing-with-python/) including all assigments.

Note! This training requires its own env file. It did not run in the concepts directory with default .venv file.

## Changes/Adaptations done to make it work on my machine

- create sandbox environment env
- load environent
- install as executable to monitor changes. Note it works with environment.yml file

```bash
pip install -e .
```

- install pytest in this env

```bash
pip install pytest
pip install pytest-cov
```

- run test using python module command, otherwise module is not found

```bash
python -m pytest
```

- created requirements.txt file

After exiting local env and starting it again I am avaliable to just run pytest.

## Lessons learned

To run just one test from the suite

```bash
# run just this test method from the suite
pytest -k test_plotting_meteogram_defaults

```

### Testing floating point values

Testing math functions with floating points can be problem. When using only pytest you can assert on small difference between actual and expected number.

```python
#
def test_floating_substractions():
    # setup
    expected = 0.01
    # excersize
    calculated = 1 - 0.99
    # verify difference due to floating point numbers
    assert abs(calculated - expected) < 0.0001
```

`Hoewer numpy has its own testing sweet for testing the numbers. This is advised approach`

```python
from numpy.testing import assert_almost_equal

def test_floating_substractions():
    # setup
    expected = 0.01
    # excersize
    calculated = 1 - 0.99
    # verify difference due to floating point numbers
    # assert abs(calculated - expected) < 0.0001
    # numpy has its own assertion suite for number
    assert_almost_equal(calculated,expected, decimal=3)

```

Numpy has also similair function for testing numpy arrays.

### Test coverage

```bash
# show test coverage rapport for module
pytest --cov-report term-missing --cov=meteogram

```

### Image testing

```bash
# run test and generate test image to be saved for later testruns
# tests/baseline folder is default location
pytest -k test_plotting_meteogram_defaults --mpl-generate-path=meteogram/tests/baseline

# run image test
pytest --mpl

```

### Fixtures
