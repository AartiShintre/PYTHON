n=int(input("enter no"))
print("MENU\n1.squre\n2.cube\n3.positive or negative\n")
ch=int(input("enter choice"))
if ch==1:
    print("squre is",n**2)
if ch==2:
    print("cube is",n**3)
if ch==3:
    if n%2==0:
        print("positive")
    else:
        print("negative")
