# Largest exponential
#
# Using base_exp.txt, a 22K text file containing one thousand lines with a
# base/exponent pair on each line, determine which line number has the
# greatest numerical value.
with open('../sources/base_exp.txt') as f:
    source = f.read()

from math import log

def calc(line):
    a,b = [int(i) for i in line.split(',')]
    return log(a)*b

nums = [ calc(line) for line in source.splitlines()]

index = max(enumerate(nums), key=lambda x: x[1])[0]

print(index+1)
# output: 709
