import json
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
user=User('max',23)
def encodeuser(o):
    if isinstance(o,User):

        return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    else:
        raise TypeError("object not found")
userjson=json.dumps(user,default=encodeuser)
print(userjson)                        