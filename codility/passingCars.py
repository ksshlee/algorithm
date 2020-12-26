def solution(A):
    zero_count = 0

    ans = 0

    for i in A:
        if i == 0:
            zero_count+=1
        else:
            ans+=zero_count
        

        if ans > 1000000000:
            return -1

    
    return ans