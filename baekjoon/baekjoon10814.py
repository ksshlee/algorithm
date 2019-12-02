#baekjoon10814 나이순 정렬

loop = int(input())

result={}


for i in range(loop):#loop번 반복
    age,name=input().split(" ") # 공백 기준으로 2개 입력받음
    age=int(age)#a를 정수로 치환
    if result.get(age) != None: #같은 나이가 이미 있는 경우
        result[age]+=" "+name #공백을 포함하여 이름을 넣어줌
    else:
        result[age]=name



#딕셔너리 정렬
def f1(x):
    return x[0]

result = sorted(result.items(),key=f1)




ans=[]#정답을 담을 리스트

for i in result:
    age=0
    for j in i:
        if isinstance(j,int)==True:#만약 int형이면 나이로 초기화 후 continue
            age=j
            continue #밑에 코드 실행되는것을 방지
        if " " in j: #  공백 즉 여러개의 이름이 들어가있는 경우
            name=j.split(" ") #공백을 기준으로 분리 name 리스트에 저장
            for k in name:
                ans.append(str(age)+" "+k)
        else:
            ans.append(str(age)+" "+j)

for i in ans:
    print(i)