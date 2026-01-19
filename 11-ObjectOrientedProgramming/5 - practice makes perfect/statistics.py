class Statistics:
    def __init__(self):
        self.number_set = []
    
    def add_number_to_set(self,number_to_add):
        self.number_set.append(number_to_add)
    
    def display_numbers(self):
        for element in self.number_set:
            print(element , end=" ")
        print()
    
    def find_biggest_number(self):
        return max(self.number_set)

    
    def find_smallest_number(self):
        return min(self.number_set)
    
    def find_arithmetic_mean(self):
        sum = 0
        for element in self.number_set:
            sum += element
        return sum / len(self.number_set)
    
    def find_median(self):
        sorted_numbers = sorted(self.number_set)
        n = len(sorted_numbers)
        middle = n // 2
        if n % 2 == 0:
            return(sorted_numbers[middle-1] + sorted_numbers[middle] / 2)
        else:
            return sorted_numbers[middle]
    
    def print_statistics(self):
        print("Minimum:", self.find_smallest_number())
        print("Maximum:", self.find_biggest_number())
        print("Arithmetic mean:", self.find_arithmetic_mean())
        print("Median:", self.find_median())

        


set1 = Statistics()

set1.add_number_to_set(12)
set1.add_number_to_set(37)
set1.add_number_to_set(6)
set1.add_number_to_set(9)
set1.add_number_to_set(17)

set1.display_numbers()
set1.print_statistics()