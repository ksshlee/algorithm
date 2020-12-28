def solution(S):
    # 기호로 저장
    stck = []

    for i in S:
        if i == '{' or i == '(' or i =='[':
            stck.append(i)
        else:
            if len(stck) == 0:
                return 0
            

            if i == '}':
                if stck[-1] == '{':
                    stck.pop()
                else:
                    return 0

            elif i == ')':
                if stck[-1] == '(':
                    stck.pop()
                else:
                    return 0

            else:
                if stck[-1] == '[':
                    stck.pop()
                else:
                    return 0

    
    if len(stck) == 0:
        return 1
    else:
        return 0
