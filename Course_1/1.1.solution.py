import sys

digit_string = sys.argv[1]
massive = list(digit_string)
result = 0
for num in massive:
    result += int(num)
print(result)
