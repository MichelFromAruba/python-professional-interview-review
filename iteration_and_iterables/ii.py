# list comprehension
from math import factorial

f = [len(str(factorial(x))) for x in range(20)]

print(f)


s = {len(str(factorial(x))) for x in range(20) if x == 19}


print(s)