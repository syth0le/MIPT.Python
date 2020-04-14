import sys

digit_string = sys.argv[1]
height = int(digit_string)
i = 1
while i <= height:
    print(" " * (height - i) + "#" * i)
    i += 1
