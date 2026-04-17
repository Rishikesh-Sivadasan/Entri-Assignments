
import random

class BankAccount:

    def new_account_creation(self):
        self.name = input("\n Please provide Account holder name: ")
        self.phone = input("\n Please enter Account holder phone number: ")

        self.account_number = random.randint(1000,9999)
        self.account_balance = 0

        print (f'''\n Your new Account is opened!!! \n
        Account number: {self.account_number}\n
        Name: {self.name}\n
        Phone number: {self.phone}\n'''
        )

        print("Please deposit a initial amount to the account")
        self.money_deposit()



    def account_check(self):

        self.acc_number = int(input("\nEnter your Account number to verify: "))

    def money_deposit(self):
    
        while True:
        
            self.account_check()

            if self.acc_number == self.account_number:

                print(f'''\nHello {self.name}''')
                self.deposit_amount = int(input("\n Please enter the deposit amount: "))
                self.account_balance = self.account_balance + self.deposit_amount

                print (f'''\nYour Account balance is: ${self.account_balance} 
                 ''')
                
                break

            else:
                print("Entered account number is incorrect !! Please enter correct account number")
                continue
            
    def money_withdrawal(self):

        while True:

            self.account_check()

            if self.acc_number == self.account_number:
                self.withdrawal_amount = int(input("Enter wihtdrawal amount:"))

                if self.withdrawal_amount <= self.account_balance:

                    self.account_balance= self.account_balance-self.withdrawal_amount
                    print(f'''\n {self.withdrawal_amount} deducted from Account: {self.acc_number}!! \n Account balance: {self.account_balance}\n Thank you !!! ''')
                    break
        
                else:
                    print("\nYou account balance is less than the entered amount, please re-try!!!\n")
                    continue

            else:
                print("Entered account number is incorrect !! Please enter correct account number")
                continue


    def balance_check(self):
        
        while True:
            self.account_check()

            if self.acc_number == self.account_number:
                print (f'''Your Account balance is: ${self.account_balance} ''')
                return
        


    def RKS_bank (self):

        while True:
            
            choose = int(input("\nPlease choose your option from below:\n\n 1. New Account \n 2. Money Withdrawal \n 3. Balance enquiry \n 4. Exit \n"))

            if choose == 1:
                self.new_account_creation()

            elif choose == 2:
                self.money_withdrawal()
            
            elif choose ==3:
                self.balance_check()
            
            elif choose ==4:
                
                print("Exit from RKS bank app!!!")
                break           
                

            elif choose not in {1,2,3,4}:
                print("\nPlease enter a valid option")
                continue



acc = BankAccount()
acc.RKS_bank()