def word_count():
    # Python program to count word occurrence

    str=input("enter ur string: ")
    wrd="python"
    count=0

    str=str.lower()
    wrd=wrd.lower()

    arr=str.split(" ")

    for i in range(len(arr)):
        if arr[i]==wrd:
            count+=1

    print(f"count of word {wrd} is: {count}")

if __name__=="__main__":
    word_count()