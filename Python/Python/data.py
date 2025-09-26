import json
# From json to python
mydict = '{"Name":"Somit","Age":"19","Class":"12"}'
x = json.loads(mydict)
print(x)

# From python to json
thisdict = {"Name":"Bante","Age":"20","Class":"13"}
y = json.dumps(thisdict,indent = 4,sort_keys=True)
print(y)



