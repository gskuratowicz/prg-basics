class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    
    def print_receipt(self):
        print(f"Distance traveled: {self.distance}km, rate: {self.rate_per_km} per km, fare: €{self.fare}")


def main():
    taxiride1 = TaxiRide(2)
    taxiride2 = TaxiRide(1.5)
    
    taxiride1.calculate_fare(10)
    taxiride2.calculate_fare(7)

    taxiride1.print_receipt()
    taxiride2.print_receipt()
    
if __name__ == "__main__":
    main()
