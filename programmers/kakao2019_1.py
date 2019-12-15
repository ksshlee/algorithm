def solution(record):
    answer = []
    uid={}

    temp=[]

    for i in record:
        tmp=i.split(" ")
        if tmp[0]=="Enter":
            temp.append(['Enter', tmp[1]])
            uid[tmp[1]]=tmp[2]
        elif tmp[0]=="Leave":
            temp.append(['Leave',tmp[1]])
        else:
            uid[tmp[1]]=tmp[2]

    for i in temp:
        if i[0]=="Enter":
            answer.append(uid.get(i[1])+"님이 들어왔습니다.")
        else:
            answer.append(uid.get(i[1])+"님이 나갔습니다.")
    
    return answer




print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))