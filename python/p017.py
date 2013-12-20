# Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?


trans = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen',
    18: 'eighteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    80: 'eighty',
}

def to_list(n):
    l = []
    while n>0:
        l.append(n%10)
        n //= 10
    return l

def words(n):
    ns = to_list(n)
    wordlist = [trans[i] for i in ns]
    if 9 < (n % 100) < 20:
        if ns[0] in [0,1,2,3,5,8]:
            wordlist[1] = trans[n % 100]
        else:
            wordlist[1] = trans[n % 10] + "teen"
        wordlist[0] = ''

    elif n >= 20 and ns[1] != 0:
        if ns[1] in [2,3,4,5,8]:
            wordlist[1] = trans[ns[1]*10]
        else:
            wordlist[1] += "ty"

    if n > 99 and ns[2] != 0:
        wordlist.insert(2, "hundred")

    if n > 99 and n % 100 != 0:
        wordlist.insert(2,"and")

    if n > 999:
        wordlist.insert(3,"thousand")

    return ' '.join(list(reversed([i for i in wordlist if i != ''])))

total = 0
for n in range(1,1001):
    total += len([c for c in words(n) if c.islower()])
print(total)

# output: 21124
