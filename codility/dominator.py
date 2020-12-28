def solution(A):
    
    if len(A) == 0:
        return -1

    def divide(B):
        if len(B) == 1:
            return B[0]


        half_num = int(len(B)/2)

        left_half = divide(B[0:half_num])
        right_half = divide(B[half_num:])

        left_count = B.count(left_half)
        right_count = B.count(right_half)

        if left_count>len(B)/2:
            return left_half
        elif right_count>len(B)/2:
            return right_half
        else:
            return None

    half_num = divide(A)

    if half_num == None:
        return -1
    
    return A.index(half_num)