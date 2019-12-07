#input 속도 가속을 위해서
import sys
input=sys.stdin.readline

working={}

for i in range(int(input())):
    text=input().strip().split(" ")
    if text[1] == 'enter':
        working[text[0]]=True
    elif text[1] == 'leave':
        working[text[0]]=False

ans=[]

#True인 애들만 모음
for i in working:
    if working[i]==True:
        ans.append(i)

#내림차순 정렬
ans.sort(reverse=True)

for i in ans:
    print(i)
