# Distinct powers
#
# How many distinct terms are in the sequence generated by ab for 2 <= a <=
# 100 and 2 <= b <= 100?

rg = range(2,101)
print(len(set(a**b for a in rg for b in rg)))
# output: 9183