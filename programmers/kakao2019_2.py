def solution(N, stages):
    answer = []
    tmp={}

    stages.sort()

    #사용자들의 각각 도전 스테이지 계산
    for i in stages:
        if tmp.get(i)==None:
            if(i>N):
                continue
            else:
                tmp[i]=1
        else:
            tmp[i]+=1

    #1부터 N까지 스테이지 tmp에 채워졌는지 확인 안채워졌으면 채워넣기
    for i in range(1,N+1):
        if tmp.get(i)==None:
            tmp[i]=0
        


    count=len(stages)
    for key in tmp:
        if tmp[key] == 0:
            answer.append([0,key])
        else:
            answer.append([tmp[key]/count,key])
            count-=tmp[key]

    #실패율 기준 내림차순 실패율이 같을시 스테이지 로 오름차순 정렬
    answer.sort(reverse = True,key=lambda a:(a[0],-a[1]))
    #찐들만 모아놓은다
    real =[]
    for i in answer:
        real.append(i[1])

    return real

print(solution(4,[4,4,4,4,4]))