# Unit testing

Basic example of unit testing. The convention is to call test files test\_`file to test`.py

## Unit test

Default testing lib is [unittest](https://docs.python.org/3/library/unittest.html).

We use this lib in the example of chain.py file.

## Running test

We run unittest module with the test file name we want to test.

```python
# run test file for chain
python -m unittest test_chain.py

```

To run test module directly by running the file we can add this lines to the file

```python
# call testmodule main to start
if __name__=='__main__':
  unittest.main()
```
