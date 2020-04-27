# Recursion

This is function that calls itself recursively and returns:

- intermediate solutions to itself
- end solution to caller

## Blueprint

Recursive function has 2 parts:

- repetitive part that calls the function
- base case that returns solution and `breaks` recursion pattern

## Pros and cons

- Pros:

  - compact codebase
  - only possible way, though sometimes loop can be used
  - with memoization can perform better than loops

- Cons:
  - complexer setups might be difficult to understand by other programmers
  - callstack size limit (some programms) and memory consumption

## Examples

### Factorial recursive function

Make function to sum factorial. For example:

- factorial(7) should sum up 7*6*5*4*3*2*1 and return result
- factorial(99) should sum up 99*98*97*96...*1 and return result

### Fibonacci sequence

Make a function which calculates fibonacchi sequence.
Fibonacci sequence look like this: 0, 1, 2, 3, 5, 8, 13, 21 ...
[More info](https://www.mathsisfun.com/numbers/fibonacci-sequence.html)

Fn = Fn-1 + Fn-2

result = fibonacci(7)
