context="my name is anant"
answer="anant lives in Amona"

cw=set(context.lower().split())
aw=set(answer.lower().split())

hallu=aw-cw

hallu_score= len(hallu)/len(aw)
print(hallu_score)