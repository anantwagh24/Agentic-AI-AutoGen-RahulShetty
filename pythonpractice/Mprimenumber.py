def check_prime():
    num = int(input("enter your number: "))

    prime_num  = True

    if num<=1:
        prime_num = False
    else:
        for i in range(2, num):
            if num%i==0:
                prime_num = False
                break
    if prime_num:
        print("Prime")
    else:
        print("Not Prime")

check_prime()
