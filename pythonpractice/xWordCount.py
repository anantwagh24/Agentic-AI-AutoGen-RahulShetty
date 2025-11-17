str=input("enter your string: ")
wrd=input("enter your word: ")

str=str.lower()
wrd=wrd.lower()

arr=str.split(" ")
count=0
for i in range(len(arr)):
    if arr[i]==wrd:
        count+=1
print(f"word count of '{wrd}' is: {count}")