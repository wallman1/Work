class BankAccount:
    def __init__(self, AccountNumber, Balance, Owner_name):
        self._AccountNumber = AccountNumber
        self._Balance = Balance
        self._Owner_name = Owner_name

    def getname(self):
        return self._Owner_name
    
    def getnum(self):
        return self._AccountNumber
    
    def getbalance(self):
        return self._Balance
    
    def set_name(self, new_name):
        if isinstance(new_name, str):
            self._Owner_name = new_name
        else:
            raise ValueError("Name must be a string.")
        
    def set_num(self, new_num):
        if isinstance(new_num, int):
            self._AccountNumber = new_num
            if 100000 <= new_num >= 1000000:
                raise ValueError("Number must have 6 digits")
        else:
            raise ValueError("Number must be an integer")
        
    def set_balance(self, new_balance):
        if isinstance(new_balance, float) or isinstance(new_balance, int):
            self._Balance = new_balance
        else:
            raise ValueError("Balance must be an integer or decimal")
    
    def remove(self, amount):
        if isinstance(amount, int):
            if amount <= self._Balance:
                self._Balance = self._Balance - amount
                return self._Balance
            else:
                return("Funds insufficent")
        else:
            raise ValueError("Withdrawal must be an integer")
        
    def deposit(self, amount):
        if isinstance(amount, int):
            self._Balance = self._Balance + amount
            return self._Balance
        else:
            raise ValueError("Deposit must be an integer")

    