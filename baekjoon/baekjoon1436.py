testcase=int(input())

books={}

for i in range(testcase):
    book=input()
    if books.get(book)==None:
        books[book]=1
    else:
        books[book]+=1

def f1(x):
    return x[1]

res = sorted(books.items(), key=f1, reverse=True)

max=res[0][1]

ans=[]

#if max same append to ans
for i in res:
    if i[1]==max:
        ans.append(i[0])
    elif i[1]<max:
        break

ans.sort()

print(ans[0])