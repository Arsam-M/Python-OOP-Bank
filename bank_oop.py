class Account:
    def __init__(self, name, password, balance=0):
        self.name=name
        self.password=password
        self.balance=balance
             
    def deposit(self, amount):
        if amount < 0:
            print('amount should be more than 0')
            return
        self.balance += amount
        print(f"{self.name}'s new balance={self.balance}")
        
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount
            print(f"{self.name}'s new balance={self.balance}")
            return True
        return False
            
    def show_balance(self):
        print(self.balance)
        
        
class Bank:
    def __init__(self):
        
        self.accounts={}
        
        
    def create_account(self, name, password):
        if name in self.accounts:
            print("account already exists")
            
        new_account=Account(name, password)
        self.accounts[name]=new_account
        print(f'the account for {name} was created')
        
    
    def transfer(self, sender_name, receiver_name, amount):
        if sender_name not in self.accounts:
            print("one of the accounts doesn't exist")
            return
        
        sender=self.accounts[sender_name]
        receiver=self.accounts[receiver_name]
        
        if sender.withdraw(amount):
            receiver.deposit(amount)
            print(f'transfer successful! {amount} from {sender_name} to {receiver_name}')
        else:
            print('insufficient funds or invalid amount')
            
            
    def show_all(self):
        for name, acc in self.accounts.items():
            print(f'{name}:{acc.balance}')
    
        
if __name__ == "__main__":
    print("--- Testing the Bank System ---")
    
    my_bank = Bank()
    my_bank.create_account("User1", "1234")
    my_bank.create_account("User2", "5678")
    
    my_bank.accounts["User1"].deposit(1000)
    my_bank.transfer("User1", "User2", 300)
    
    my_bank.show_all()