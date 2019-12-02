#baekjoon 1316 그룹 단어 체커

a = int(input())

count=0

for i in range(a):#사용자가 원하는 만큼 반복
    check = {}
    test = input() #단어 입력받고
    flag=""
    notword=False
    for j in test:
        if flag!=j: #전 단어와 같지 않으면 flag값을 현재로 바꿈
            flag=j
            getnum = check.get(j)
            if getnum!=None:
                notword=True
                break
            check[j]=1
        else:
            check[j]=1
    
    if notword==False:
        count+=1

print(count)
