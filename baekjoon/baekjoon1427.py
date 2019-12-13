text=input()
ans=""
tmp=[]
for i in text:tmp.append(i)
tmp.sort(reverse=True)
for i in tmp:ans+=i
print(ans)