# Calculator

A Python calculator practice project with reusable math functions in `calculator.py`.

This repo is a lightweight learning project, but it already includes a working Python module with basic and scientific calculator operations.

## Features

- Addition, subtraction, multiplication, and division
- Power and square root
- Modulus and floor division
- Logarithms
- Trigonometric functions: sine, cosine, tangent
- Factorial
- Absolute value, rounding, min/max, and average helpers
- Defensive checks for invalid operations such as division by zero, negative square roots, and invalid logarithms

## Project Structure

```text
calculator/
├── calculator.py   # Calculator functions
└── README.md       # Project documentation
```

## How to Use

Import the functions from `calculator.py` in a Python script or interactive session:

```python
from calculator import adittion, division, square_root

print(adittion(2, 3))      # 5
print(division(10, 2))     # 5.0
print(square_root(16))     # 4.0
```

Note: `adittion` keeps the original misspelled function name used in the source file.

## Purpose

- Practise Python functions and math operations
- Add defensive error handling for invalid inputs
- Keep a small reusable module for experimentation
- Document a simple practice project clearly

## Suggested Next Steps

- Add unit tests for each calculator operation
- Add a command-line interface for interactive calculations
- Rename `adittion` to `addition` while keeping a compatibility alias
- Add type hints for function arguments and return values

## Portfolio Note

For stronger examples of my current work, see:

- [Meeting Platform](https://github.com/franng95/meeting_platform)
- [University Assistant Chatbot](https://github.com/franng95/Chatbot-Flet)
- [Now Fitness](https://github.com/franng95/NowFitness)
- [Advanced Algorithms](https://github.com/franng95/advanced-algorithms)