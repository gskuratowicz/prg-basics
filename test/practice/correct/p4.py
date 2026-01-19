class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        result = self.name[0] + "-" + str(self.age)
        if self.age < 18:
            return result.lower()
        else:
            return result.upper()
        
if __name__ == "__main__":
    print(C("John",18))
    print(C("Anna",17))