#!/usr/bin/python3
if __name__ == "__main__":
    import sys

num_args = len(sys.argv) - 1
if num_args != 0:
    print(f"{num_args} arguments:")
    for i in range(num_args):
        print(f"{i}: {sys.argv[i + 1]}")
else:
    print(f"{num_args} arguments.")
