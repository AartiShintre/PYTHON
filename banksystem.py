print("MENU =>\n1.Check Balance\n2.Deposite Money\n3.Withdraw Money\n4.Exit")
ch=int(input("enter choice"))
if ch==1:
    intial_balance=1000
    print("Your Balance is",intial_balance)
if ch==2:
    d_balance=int(input("enter amount to deposited"))
    new_balance=d_balance+intial_balance
    print("your balance",new_balance)
if ch==3:
    w_balance=int(input("enter amount to withdraw"))
    new_balance2=new_balance-w_balance
    print("your balance",new_balance)
if ch==4:
    print("exit")
