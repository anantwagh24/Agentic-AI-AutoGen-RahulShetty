# input as 10 , reverse it to 1, 10 should be in the output

class Solution:

    n=int(input("enter your number: "))


    for i in range(n,0,-1):
        n-=1
        print(n+1 ,end=" ")

    # while num>0:
    #     num-=1
    #     print(num+1, end=" ")