import json
person={"name":"huge",'class':23,'age':12}
personjson=json.dumps(person,indent=4,sort_keys=True)
print(personjson)

with open('person.json','w') as file:
    json.dump(person,file,indent=4)