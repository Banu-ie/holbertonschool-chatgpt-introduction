# Debugging Exercises

This directory contains corrected versions of several debugging exercises involving Python, HTML, and JavaScript. Each section explains the issue found in the original code and the fix that resolves it.

---

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

---

# Python Arguments Debugging

## Issue

The script printed all values from `sys.argv`, including the script name (`print_arguments.py`).

## Fix

Skip the first element of `sys.argv`, which contains the script name.

```python
for arg in sys.argv[1:]:
    print(arg)
```

This prints only the user-provided arguments.

---

# HTML / JavaScript Background Color Debugging

## Issue

The button ID in HTML was misspelled (`colorButon`) while the JavaScript tried to access `colorButton`. Because of this mismatch, the click event was never triggered.

## Fix

Correct the button ID so it matches the JavaScript selector.

```html
<button id="colorButton">Change Color</button>
```

Now the click event correctly triggers the background color change.

---

# Python Mines Debugging

## Issue

The game did not detect when the player had successfully revealed all non-mine cells. As a result, the game could never be won.

## Fix

Add a function to check if all safe cells have been revealed.

```python
def check_win(self):
    for y in range(self.height):
        for x in range(self.width):
            if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                return False
    return True
```

Call this function after each move to determine if the player has won.

---

# Python Recursive Factorial Documentation

## Issue

The function had indentation errors and lacked documentation explaining its purpose and usage.

## Fix

Correct the indentation and add a docstring describing the function, its parameters, and its return value.

```python
def factorial(n):
    """
    Function description:
        Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.
    """
```

This improves readability and ensures the code executes correctly.

---

# Python Checkbook Error Handling

## Issue

The program crashed when the user entered a non-numeric value for deposit or withdrawal amounts.

Example error:

```text
ValueError: could not convert string to float
```

## Fix

Wrap the input conversion in a `try/except` block to handle invalid inputs gracefully.

```python
try:
    amount = float(input("Enter the amount: "))
except ValueError:
    print("Invalid amount. Please enter a numeric value.")
```

This prevents the program from crashing and allows the user to try again.

---

# Python Tic Tac Toe Debugging

## Issue

Several problems existed in the original implementation:

- The program could crash with invalid input.
- The wrong player could be declared the winner.
- No detection for a draw condition.
- The board formatting was inconsistent.

## Fix

Add input validation, detect when the board is full, and ensure the correct player is declared the winner.

Example input validation:

```python
try:
    row = int(input("Enter row: "))
    col = int(input("Enter column: "))
except ValueError:
    print("Invalid input. Please enter numbers only.")
```

This ensures the game handles user input safely and behaves correctly.
