# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # 숫자 등장 여부 0이면 미등장 1이면 등장
    max_num = max(A)

    initialize_num = max(max_num,len(A))

    # 최대값이 음수면 1이 답
    if max_num>0:
        numbers = [0] * initialize_num
    else:
        return 1

    for i in A:
        # 양수면
        if i>0:
            numbers[i-1]+=1


    for idx,number in enumerate(numbers):
        if number == 0:
            return idx+1
    
    return len(A)+1

