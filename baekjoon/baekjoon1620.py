nums,question=input().split(" ")

monster={}
for i in range(1,int(nums)+1):
    text=input()
    #숫자와, 이름을 각각 키로 만들어서 dict에 저장
    monster[text]=i
    #질문할때 숫자도 str로 받으므로 str로 저장
    monster[str(i)]=text

ans=[]

for i in range(int(question)):
    text=input()
    #결과를 저장
    ans.append(monster.get(text))

for i in ans:print(i)