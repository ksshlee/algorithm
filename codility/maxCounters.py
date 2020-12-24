def solution(N, A):
    # write your code in Python 3.6
    # N 개의 배열을 0으로 초기화
    counter = [0] * N

    max_value = 0

    tmp_max = 0

    for i in A:
        if i == N+1:
            # N+1 이 들어 왔을때
            # max_value 로 초기화
            tmp_max = max_value
        else:

            # 한번에 계산하는 것이 아닌
            # 계속 체크하면서 계산
            if counter[i-1] < tmp_max:
                counter[i-1] = tmp_max


            counter[i-1]+=1

            if max_value < counter[i-1]:
                max_value = counter[i-1]


    # 마지막으로 tmp_max 보다 작은 값 확인
    for i in range(len(counter)):
        if counter[i]<tmp_max :
            counter[i] = tmp_max



    return counter