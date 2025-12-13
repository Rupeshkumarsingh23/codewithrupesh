account={101:50000,102:45000,103:55000}
account_id=int(input("Enter account id:"))
amount=int(input("Enter amount:"))
if account_id in account:
    account[account_id]=account[account_id]+amount
else:
    account[account_id]=amount
print("account details:")
for account_id,amount in account.items():
    print(account_id,amount)
