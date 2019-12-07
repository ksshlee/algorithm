def solution(letter):
    flag = letter[0] #알파벳 변하는걸 확인
    count=1 #알파벳 글자수 새기위한

    letter_count=[]

    #알파벳 글자수 측정

    for i in letter[1:]:#0은 flag이니깐 1부터 검사
        if i == flag:#현재 포인터가 flag랑 같으면 알파벳 갯수 +1
            count+=1
        else:#다르면
            letter_count.append([flag,count])#알파벳과 갯수 저장
            flag=i #flag값 변동
            count=1#개수  초기화

    letter_count.append([flag,count])#마지막 알파벳도 저장

    letter_count.sort()#알파벳 순으로 정렬


    left=[] #팰린드롬 왼쪽 글자
    center=[] #팰린드롬 가운데
            
    for i in letter_count:
        if i[1]%2==0:#짝수
            for j in  range(i[1]//2):
                left.append(i[0])
        else:#홀수
            if(len(center)!=0):
                return "I'm Sorry Hansoo"#홀수가 2개이상이면
            for j in range(i[1]):
                center.append(i[0])

    #AAABB ==> ABABA 이럴때 하기 위한 것
    if len(center)>=3:#center의 길이가 3이상이다
        for i in range(len(left)):
            if center[0]<left[i]:#left 보다 center의 알파벳이 작으면
                left.insert(i,center[0]*int(len(center)//2))#작은곳에 center의 2로 나눈 몫만 추가
                center=[center[0]]#센터 초기화

    right=left[::-1] #reverse

    ans=""

    for i in left+center+right:
        ans+=i

    return ans


letter = input()

letter_to_list=[]

#문자하나하나씩 리스트에 넣어줌
for i in letter:
    letter_to_list.append(i)

letter_to_list.sort()
print(solution(letter_to_list))