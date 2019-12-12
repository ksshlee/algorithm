#java로 변환
def tojava(text):
    #첫 문자가 _일때
    if text[0] == "_":
        return "Error!"


    #마지막 문자가 _일때
    if text[-1] == "_":
        return "Error!"
    
    ans=""
    flag=False
    for i in text:
        #대문자 일때
        if ord(i)>=65 and ord(i)<=90:
            return "Error!"

        #_가 연속해서 나올때
        if i=="_" and flag==True:
            return "Error!"

        if i == "_":
            flag = True
            continue

        if flag == True:
            ans += i.upper()
            flag=False
            continue

        ans+=i

    return ans
        

#c++로 변환
def toc(text):
    #첫 문자가 대문자 일때
    if ord(text[0])>=65 and ord(text[0])<=90:
        return "Error!"

    ans=""

    for i in text:
        #대문자 일때
        if ord(i)>=65 and ord(i)<=90:
            ans+="_"+i.lower()
        else:
            ans+=i


    return ans



text = input()

if "_" in text:
    print(tojava(text))
else:
    print(toc(text))