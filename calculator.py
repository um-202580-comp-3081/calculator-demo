#!/usr/bin/env python3
import sys


def usage():
    print(
        """
usage: calculator.py [-v] EXPR
       EXPR: valid mathematical expression to evaluate
options:
  -v            verbose mode
""",
        file=sys.stderr,
    )


"""
Test Cases

Expected Success:
./calculator.py "1 + 2"

Expected Failure:
./calculator.py

"""

if len(sys.argv) < 2:
    print("error: not enough arguments")
    usage()
    sys.exit(1)


expr = sys.argv[1]


def calculate(expr):
    print(eval(expr))


calculate(expr)
