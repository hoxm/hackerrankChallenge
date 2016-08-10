#!/bin/python3

import sys

N = int(input().strip())

if N < 1:
    print("Out of range (1 <= N <= 100)")
elif N % 2 == 1:
    print("Weird")
elif N <= 5:
    print("Not Weird")
elif N <= 20:
    print("Weird")
elif N <= 100:
    print("Not Weird")
else:
    print("Out of range (1 <= N <= 100)")
