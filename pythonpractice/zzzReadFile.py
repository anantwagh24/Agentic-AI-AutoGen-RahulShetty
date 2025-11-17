from pathlib import Path

file=Path("/Users/anantwagh/Downloads/long-doc.txt").read_text()
print(file)

wrd=input("enter word: ")

file=file.lower()
wrd=wrd.lower()

words=file.split()

count=0
for i in range(len(words)):
    if words[i]==wrd:

        count+=1
print(f"word {wrd} appears {count} times")