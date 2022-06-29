from itertools import combinations_with_replacement, product,permutations,combinations ,combinations_with_replacement
from re import X
import operator
a=[1,2]
b=[3]
prod=product(a,b)
print(list(prod))
prod=product(a,b,repeat=2)
print(list(prod))
 

X=[1,2,3]
perm=permutations(a)
print(list(perm))

m=[1,2,3,4]
comb=combinations(m,2)
print(list(comb))
comb_wr=combinations_with_replacement(a,2)
print(list(comb_wr))

