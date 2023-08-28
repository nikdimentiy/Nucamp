"""
This program prints "Hello, my name is <argument>" for each argument passed to the program.

Usage:
    python hello_name.py <argument>

Example:
    python hello_name.py Nikey

Output:
    Hello, my name is Nikey
"""

import sys


def main():
    """The main function."""
    if len(sys.argv) < 2:
        sys.exit("To few arguments.")

    for arg in sys.argv[1:]:
        print("Hello, my name is", arg)


if __name__ == "__main__":
    main()

