testa,testb = input().split(" ")

ans={}

a=[]

for i in range(int(testa)):
    text=input()
    ans[text]=True
for i in range(int(testb)):
    text=input()
    if ans.get(text)!=None:
        if(ans[text]==True):
            a.append(text)
    else:
        continue

print(len(a))
a.sort()
for i in a:
    print(i)