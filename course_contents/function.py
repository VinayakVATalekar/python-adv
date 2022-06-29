
def prime(x):
     
    for i in range(2,x):
        
        if x%i==0:
            return "not prime"
    return 'prime'    



x=int(input("enter a nno"))
if x>2:
    print(prime(x))
elif x==2:
    print('prime')
else:
    print('not prime')