api_response = {
    "firstname" : "shrenik Mehta",
    "age" : 25,
    "password" : "Shrenik@123"

}

print(api_response)
print(type(api_response))
print(api_response.get('age'))

for key ,value in api_response.items():
    print(key, " -->> ",value)