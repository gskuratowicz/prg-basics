class BankAccount:
    def __init__(self,acc_number):
        self.account_balance = 0
        self.acc_number = str(acc_number)
    
    def deposit(self,amount_to_deposit):
        self.account_balance += amount_to_deposit

    def withdraw(self,amount_to_withdraw):
        if amount_to_withdraw <= self.account_balance:
            self.account_balance -= amount_to_withdraw
        else:
            print("Insufficient funds on the account.\n")
    
    def display_info(self):
        print(f"Bank account No: {self.acc_number[:2] + " " + self.acc_number[2:6] + " " + self.acc_number[6:10] + " " + self.acc_number[10:14] + " " + self.acc_number[14:18] + " " + self.acc_number[18:22] + " " + self.acc_number[22:26]}\nBalance: PLN  {self.account_balance}\n")