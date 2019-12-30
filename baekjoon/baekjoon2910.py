text = input().split(" ")
num=input().split(" ")

num_count={}

for i in num:
    if num_count.get(i)==None:
        num_count[i]=1
    else:
        num_count[i]+=1

ans=sorted(num_count.items(),reverse=True,key=lambda x:x[1])

string=""

for i in ans:
    string += (i[0]+" ")*i[1]

print(string)