car = {
    "Year":1964, 
    "Brand":"Ford" , 
    "Model":"Mustang"
     }
     
print(car)
year = car.get("Year")
brand = car.get("Brand")
model = car.get("Model")

print("This dictionary should describe the following object:")
print(year)
print(brand)
print(model)

print("Access the dictionary to print the value of the “model” of the car.")
print(model)

# Perform Dictionary Methods on Your Object, and in a comment explain the result you expected vs the result that you got.

#returns a list containing a touple for each key value
items = car.items()
print(items)

#returns a list containing the dictionary keys
keys = car.keys()
print(keys)

#returns the value of a specific key, if the key does not exist, it inserts key and value
setdefault = car.setdefault("Color", "Blue")
print(car)

#removes the last inserted key value pair
car.popitem()
print(car)