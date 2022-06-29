from functools import reduce
a=[7,5,6,1,2,3,4]

pr=reduce(lambda x,y:x*y,a)
print(pr)
