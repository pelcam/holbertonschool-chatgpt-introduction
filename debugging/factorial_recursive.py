#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if the user provided an argument
if len(sys.argv) < 2:
    print("Usage: python3 script.py <non-negative integer>")
    sys.exit(1)

try:
    # Convert the argument to an integer
    n = int(sys.argv[1])

    # Check if the number is non-negative
    if n < 0:
        print("Error: The argument must be a non-negative integer.")
        sys.exit(1)

    # Calculate the factorial
    f = factorial(n)
    print(f)

except ValueError:
    print("Error: The argument must be an integer.")
    sys.exit(1)

