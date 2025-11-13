str=input("enter your string: ")

count=0

for ch in str:
    if ch in ("a","e","i","o","u"):
        count+=1
    print(ch, end=" ")

print(f"vowels count are: {count}")