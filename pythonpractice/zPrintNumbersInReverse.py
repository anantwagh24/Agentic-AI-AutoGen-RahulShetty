# input as 10 , reverse it to 1, 10 should be in the output
class reverse_numbers:

    num=int(input("Enter a number: "))

    for i in range(num,0,-1):
        num-=1
        print(num+1,end=" ")

    # while num>0:
    #     num-=1
    #     print(num+1, end=" ")