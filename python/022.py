# Names Scores
#
# What is the total of all the name scores in the file?

with open('../sources/names.txt', 'r') as f:
    data = f.read()

s = sorted(d[1:-1] for d in data.split(","))

total = 0
for i,name in enumerate(s):
    total += sum(ord(c) - ord('A')+1 for c in name) * (i+1)

print(total)
# output: 871198282
