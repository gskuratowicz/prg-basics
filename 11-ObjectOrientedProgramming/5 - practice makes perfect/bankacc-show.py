from bankacc import BankAccount
def main():
    my_bank_acc = BankAccount(12345655559090111100007722)
    my_bank_acc.display_info()
    my_bank_acc.deposit(25.30)
    my_bank_acc.display_info()
    my_bank_acc.withdraw(31.70)
    my_bank_acc.display_info()
    my_bank_acc.withdraw(14)
    my_bank_acc.display_info()

if __name__ == "__main__":
   main() 
