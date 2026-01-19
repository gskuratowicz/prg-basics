class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        username = ""
        if self.age >= 18:
            username += self.surname + self.name[0] + str(self.seniority)
            return username.upper()
        else:
            username += self.surname + self.name[0] + str(self.seniority)
            return username.lower()
        

print(C("Anna","May",17,7))
print(C("George","Brown",21,4))