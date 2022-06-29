import json
from textwrap import indent
person={"name":"huge",'class':23,'age':12,'ho':True}
personjson=json.dumps(person,indent=4,sort_keys=True)
print(personjson)

with open('person.json','r') as file:
    person=json.load(file)
print(person)