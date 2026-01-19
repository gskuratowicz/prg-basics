class C:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def represent_name(self):
        representation = self.first_name[0] + self.last_name[0] + str(self.age)
        if self.age < 18:
            return representation.lower()
        else:
            return representation.upper()

person1 = C("Anna","Brown",17)
person2 = C("John", "May",18)
print(person1.represent_name())
print(person2.represent_name())