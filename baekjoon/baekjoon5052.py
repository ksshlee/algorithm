import sys
input=sys.stdin.readline
testcase=int(input())#테스트케이스



def solution(result):
    flag=result[0] #비교 대상

    for i in result[1:]:
        if flag in i[0:len(flag)]:#처음부터 flag값의 길이까지 비교
            return "NO"
        else:
            flag=i#flag 값 교체

    return "YES"


ans=[]

for i in range(testcase):
    result=[]
    numofphone=int(input())#전화번호수
    for j in range(numofphone):
        phonenum=input().rstrip()#전화번호 입력받음
        result.append(phonenum)#길이, 번호 순으로 result에 저장
    result.sort()#길이순서로 정렬

    ans.append(solution(result))#solution 결과를 ans에 푸시!


for i in ans:
    print(i)

