def solution(prog, speeds):
    import math
    answer = []
    temp=[]
    #반올림 해서 날짜들 따로 저장
    for i in range(len(prog)):
        temp.append(math.ceil((100-prog[i])/speeds[i]))


    flag=temp[0]
    count=0
    for i in temp:
        #flag보다 크면 교체 및 정답list에 배포 개수 추가
        if i>flag:
            flag=i
            answer.append(count)
            #현재꺼 포함하므로 1
            count=1
        else:
            count+=1
    #마지막꺼도 추가
    answer.append(count)
    return answer



print(solution([93,30,55],[1,30,5]))