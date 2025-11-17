fruits=input("enter fruits: ").split(" ")


for i in range (len(fruits)):
    for j in range (i+1, len(fruits)):
        if fruits[i]==fruits[j]:
            print("duplicate value is: ",fruits[i])


