# Large sum
#
# work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers.

with open("../sources/p013.txt") as f:
    source = f.read()

numbers = [int(x) for x in source.splitlines()]

result = str(sum(numbers))[:10]
print(result)

# output: 5537376230
