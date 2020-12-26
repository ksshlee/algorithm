def solution(S, P, Q):
    
    result = []

    for i in range(len(P)):

        tmp = (S[P[i]:Q[i]+1])

        try:
            tmp.index('A')
            result.append(1)
        except:
            try:
                tmp.index('C')
                result.append(2)
            except:
                try:
                    tmp.index('G')
                    result.append(3)
                except:
                    result.append(4)

    
    return result