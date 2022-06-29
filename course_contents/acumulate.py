from itertools import accumulate 
import operator
#accumulation
a=[1,2,5,4,0]
print(a)
acc=accumulate(a,func=max) 
z=[1,2,3,4]
print(list(acc))
ac=accumulate(z,func=operator.mul) 
print(list(ac))