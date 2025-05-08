import BankAccount as BankAccount

account1 = BankAccount.BankAccount(193567,200010.23, "John Fogerty")

ans = input("""What would you like to do?:
      1. Check Balance
      2. Withdraw Money
      3. Deposit Money
      4. Quit
        """)
try:
    ans = int(ans)
except:
    print("answer not a number")
stop = 0
while stop == 0:
    if ans == 1:
        print(account1.getbalance())
    if ans == 2:
        amt = int(input("How much would you like to withdraw?: "))
        print(account1.remove(amt))
    if ans == 3:
        amt = input(int("How much would you like to deposit?: "))
        print(account1.deposit(amt))
    if ans == 4:
        stop = 1

    ans = input("""What would you like to do?:
      1. Check Balance
      2. Withdraw Money
      3. Deposit Money
      4. Quit
        """)