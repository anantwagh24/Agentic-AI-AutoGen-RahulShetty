import asyncio

from numpy.ma.extras import average


def sum_calculation():

    start=0
    end=100
    sum=0

    for i in range(start, end+1):
        sum+=i

    print(f"sum is: {sum}")


    average=sum/100

    print(f"average is: {average}")

if __name__ == '__main__':
    sum_calculation()