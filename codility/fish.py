def solution(A, B):
    
    stck = []

    ans = 0

    if B[0] == 0:
        ans+=1
    else:
        stck.append(A[0])


    
    for i in range(1,len(A)):
        # 만약 하류로 가는 애라면
        # 스택에 추가
        if B[i] == 1:
            stck.append(A[i])
        else:
        #상류로 가는 애라면 크기 비교
            is_clear = True

            # 비어있지 않다면
            while len(stck) != 0:
                # 더크면 상류로 올라가는애가 먹힘
                if stck[-1]>A[i]:
                    is_clear = False
                    break
                # 하류로 가는애가 먹힘
                else:
                    stck.pop()
            
            # 상류로 올라가는 애가 이겼다면
            if is_clear == True:
                ans+=1

                


    return ans + len(stck)

