class C:
    def __init__(self,sectors):
        self.sectors = sectors
    
    def m1(self,s,n): #change number of fans n in sector s/add new sector s
        self.sectors[s] = n
    
    def m2(self,s): #returns sum of the fans in the sectors listed in s string
        total = 0
        for sector in s:
            if sector in self.sectors:
                total += self.sectors[sector]
        return total



if __name__ == "__main__":
    stadium = C({"A":120,"D":150,"G":90,"K":110})
    stadium.m1("G",130)
    stadium.m1("G",0)
    print(stadium.m2("GD"))
    print(stadium.m2("KEJ"))
