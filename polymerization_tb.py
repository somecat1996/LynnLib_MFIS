from Polymerization import Polymerization

a = Polymerization([2, 3, 0, 0, 2, 1])
b = Polymerization({5: 1, 3: 2, 1: 1})
c = Polymerization([5, 3, 1], [1, 2, 1])
print(a)
print(b)
print(c)
print(b != c)
a += b
print(a)
print(a - b)
print(b / c)
print(a % b)
a.SetMod(2)
print(a)
