account={101:20000,102:30000,103:40000,105:50000}
account_id=int(input("Enter account_id:"))
amount=int(input("Enter amount:"))
balance=account.get(account_id)
if balance is None:
    account[account_id]=amount
    print("account added")
else:
    balance=balance+amount
    print("account updated")
print("after changes")
print(account)
    
    
    
               
