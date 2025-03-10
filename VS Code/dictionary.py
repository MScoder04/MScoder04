dict1={1:"pencil",2:"pen","three":[2,4,6]}
print(dict1)
dict2={"name":"Misha", "age":"15"}
print(dict2)
dict2["address"]="Georgia"
print(dict2)
dict2["age"]="16"
print(dict2)
dict1.pop(2)
print(dict1)
print(dict2.get("address"))
dict1.clear()
print(dict1)