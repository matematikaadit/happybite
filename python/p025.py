# 1000-digit Fibonacci number
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?

i = 1
a, b = 1, 1
while a < (10**999 - 1):
    a, b = b, a+b
    i += 1

print(i)
# output: 4782
