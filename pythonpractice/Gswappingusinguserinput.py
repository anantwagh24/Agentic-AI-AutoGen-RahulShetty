class swap:

    n1=int(input("enter 1st num: "))
    n2=int(input("enter 2nd num: "))

    n1=n1+n2
    n2=n1-n2
    n1=n1-n2

    print(f"numbers after swap: {n1} and {n2}")


