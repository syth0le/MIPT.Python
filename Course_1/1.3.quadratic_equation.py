import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
discriminant = b ** 2 - (4 * a * c)
x1 = ((-b - math.sqrt(discriminant)) / (2 * a))
x2 = ((-b + math.sqrt(discriminant)) / (2 * a))
print(int(x1))
print(int(x2))
