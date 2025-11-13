class clean_string:
    str=input("enter string: ")
    clean=" "

    str=str.lower()
    for ch in str:
        if ch.isalpha() or ch==" ":
            clean+=ch

    print(f"clean string is: {clean}")