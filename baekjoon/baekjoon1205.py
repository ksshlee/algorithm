arr = input().split(" ") # arr=[현재 점수 개수,송유진점수,랭킹에 올라갈수 있는 점수]


#만약 현재 점수의 개수가 0이면
if arr[0]=='0':
    print("1")
    exit()


score = input().split(" ")

#int형으로 치환
for i in range(len(arr)):
    arr[i]=int(arr[i])

for i in range(len(score)):
    score[i]=int(score[i])


if len(score)<arr[2]:
    score.append(arr[1])
    score.sort(reverse=True)
    print(score.index(arr[1])+1)
else:
    if score[-1]>=arr[1]:
        print("-1")
    else:
        score.append(arr[1])
        score.sort(reverse=True)
        print(score.index(arr[1])+1)