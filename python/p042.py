with open('../sources/words.txt') as f:
    source = f.read()

trans = { v:i for i,v in enumerate('"ABCDEFGHIJKLMNOPQRSTUVWXYZ') }
word_sums = [ sum(trans[c] for c in word) for word in source.split(',') ]

MAX = max(len(eval(w)) for w in source.split(',')) * 26 # for z

triangles = { n*(n+1)/2 for n in range(1,MAX) }

result = [ i for i in word_sums if i in triangles ]
print(len(result))