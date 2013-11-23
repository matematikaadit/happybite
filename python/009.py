#!/usr/bin/env python3

# Special Pythagorean Triplet
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# refactoring: perkecil rangenya.
#
# misalkan kita punya segitiga dengan panjang sisi-sisi a, b, dan c
# serta memiliki keliling k.
#
# untuk setiap segitiga berlaku:
#   "panjang suatu sisi selalu kurang dari jumlah dari dua sisi yang lain"
# salah satunya: a < b + c
#
# tambahkan a ke kedua ruas pertidaksamaan di atas
#     a < b + c
# a + a < a + b + c
#    2a < k
#     a < k/2
# Jadi, a < k/2
# sehingga range untuk a pada soal ini = [1,500)
#
# berikutnya, dengan menggunakan cara yang sama, kita juga akan punya:
#     c < k/2
#
# dan karena c = k - a - b, kita akan memperoleh:
# k - a - b   < k/2
# k - a - k/2 < b
#     k/2 - a < b
#
# sehingga diperoleh range untuk b pada soal ini = (500 - a, 500)
# atau (a, 500), lihat mana yang lebih besar, 500 - a atau a itu sendiri
#
# c mengikuti sisanya.

for a in range(1,500):
    down = max(a, 500 - a)
    for b in range(down,500):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print(a*b*c)

# output: 31875000
