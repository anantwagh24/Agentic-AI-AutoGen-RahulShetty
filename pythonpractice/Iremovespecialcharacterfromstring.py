
# program to trim the Special Chars and print the Alphabets:
str=input("enter string: ").lower()

clean=""

for ch in str:
    if ch.isalpha():
        clean+=ch
print(f"clean string is: {clean}")


# program to trim the Alphabets and print the Special Chars:
# str=input("enter string: ").lower()
#
# clean=""
#
# for ch in str:
#     if not ch.isalpha():
#         clean+=ch
# print(f"clean string is: {clean}")