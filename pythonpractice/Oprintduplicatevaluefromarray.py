lang=input("enter your values: ").split(",")

for i in range(len(lang)):
    for j in range(i+1, len(lang)):
        if lang[i]==lang[j]:
            print(f"duplicate value is: {lang[i]}")
