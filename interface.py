import itertools

theletters = input("Enter the letters in lowercase: ")
thenumbers = input("Enter the number of letters: ")
thenumbers = int(thenumbers)
fname = "words.txt"

lines = [line.rstrip('\n').lower() for line in open(fname)]
perms = itertools.permutations(theletters, thenumbers)
ours = [''.join(perm) for perm in perms]

values = sorted(list(set(lines) & set(ours)))

for val in values:
    print val
