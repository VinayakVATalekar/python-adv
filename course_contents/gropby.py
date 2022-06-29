from itertools import groupby,count,cycle,repeat
def smaller_than_3(x):
    return x<3


a=[1,2,3,4]
group_by=groupby(a,key=smaller_than_3)
for key,value in group_by:
    print(key,list(value))


for i in count(10):
    print(i)
    if i==15:
        break

for i in cycle(a):
    print(i)
    if i==4:
        break


for i in repeat(1,4):
    print(i)