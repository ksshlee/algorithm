def solution(arrangement):
    answer = 0
    stack=[]
    pipe_count=0
    for i in arrangement:
        if i == "(":
            stack.append(i)
            pipe_count+=1
        elif i== ")":
            if stack[-1]=="(":
                pipe_count-=1
                answer+=pipe_count
                stack.append(i)
            else:
                answer+=1
                pipe_count-=1

    return answer