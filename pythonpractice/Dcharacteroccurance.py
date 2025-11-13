from pythonpractice.LcharacterOccurence import count

string="IIIIIDIDIDIDIDIIIDSFSDFISDFISDIFSDIFSIDVIBIINIIIIIIINININIININININININ"
char='d'
count=0

string = string.lower()
char= char.lower()
print(string.lower())
print(char.lower())

for i in range(len(string.lower())):
    if string[i]==char:
        count+=1
print(f"occurance of {char} is {count} times")