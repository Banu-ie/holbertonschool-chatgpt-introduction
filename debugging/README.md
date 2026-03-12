# Python Factorial Debugging

## Issue

The program entered an infinite loop because the variable `n` was never updated inside the `while n > 1` loop.

## Fix

Decrement `n` during each iteration of the loop.

```python
while n > 1:
    result *= n
    n -= 1
```

This allows the loop to terminate and correctly compute the factorial.
