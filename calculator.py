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
./calculator.py -v "1 + 2"
./calculator.py "1 + 2" -v 

Expected Failure:
./calculator.py

"""

if len(sys.argv) < 2:
    print("error: not enough arguments")
    usage()
    sys.exit(1)


verbose = False
expr = None
i = 1
while i < len(sys.argv):
    arg = sys.argv[i]
    if arg == "-v":
        verbose = True
    else:
        expr = arg
    i += 1


def calculate(expr, verbose):
    if verbose:
        print(f"{expr} = {eval(expr)}")
    else:
        print(eval(expr))


calculate(expr, verbose)
