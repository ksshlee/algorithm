letter_count=int(input())

letter_list={}


def tmp(list_of,a):
    #중복확인
    if a in list_of != False:
        return list_of
    

    list_of.append(a)
    list_of.sort()
    return list_of 


for i in range(letter_count):
    text=input()

    if letter_list.get(len(text)) == None:
        letter_list[len(text)]=[text]
    else:
        a=tmp(letter_list.get(len(text)),text)
        letter_list[len(text)]=a


#딕셔너리 정렬
def f1(x):
    return x[0]

result = sorted(letter_list.items(),key=f1)


for i in result:
    for j in i[1]:
        print(j)