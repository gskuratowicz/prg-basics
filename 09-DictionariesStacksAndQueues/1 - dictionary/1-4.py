person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print("Name: ", person["name"] + person["surname"])
for item in person["hobby"]:
    print ("Hobby: ", item)

person["surname"] = "Nowak"
person["married"] = False
person["gender"] = "Male"
