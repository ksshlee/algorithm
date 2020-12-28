def solution(S):
    # 스택 선언 (개수로 표현)
    stck = 0

    for i in S:
        if i == '(':
            stck+=1
        else:
            # 스택에 아무것도 없으면
            if stck == 0:
                return 0
            else:
                stck-=1
    
    if stck==0:
        return 1
    else:
        return 0


