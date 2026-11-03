person={
    "name":"Abeera",
    "age":24,
    "Dept":"BSCS"
}

print(person["name"])
person["age"]=23
print(person["age"])

new_Dict={key: value for key,value in person.items()}
print(new_Dict)

