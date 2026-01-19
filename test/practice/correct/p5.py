class C:
    def __init__(self,stadium):
        self.stadium = stadium
    
    def m1(self,s,n):
        self.stadium[s] = n
    
    def m2(self,s):
        total = 0
        count = 0
        for sector in s:
            if sector in self.stadium:
                total += self.stadium[sector]
                count += 1
        return int(total / count)

if __name__ == "__main__":
    stadium = C({"A":120,"D":150,"G":90,"K":110})
    stadium.m1("G",130)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))
