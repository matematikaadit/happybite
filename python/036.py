# Double-base palindrome
#
# Find the sum of all numbers, less than one million, which are palindromic
# in base 10 and base 2.

def palindrome(s):
    return s == s[::-1]
def bstr(n):
    return "{:b}".format(n)

r = sum(n for n in range(1000000)
          if palindrome(str(n)) and palindrome(bstr(n)))
print(r)
# output: 872187
