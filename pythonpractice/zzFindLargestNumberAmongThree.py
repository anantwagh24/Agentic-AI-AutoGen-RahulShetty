class abc:
    n1=int(input("enter the first number: "))
    n2=int(input("enter the second number: "))
    n3=int(input("enter the third number: "))



    if n1>=n2 and n1>=n3 :
        greatest=n1
    elif n2>=n3 and n2>=n1 :
            greatest=n2
    else :
            greatest=n3
    print(f"greatest number is {greatest}")
