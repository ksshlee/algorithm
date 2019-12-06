first_input=input().split(" ")
len=int(first_input[0])
nth=int(first_input[1])

second_input=input().split(" ")
result=[]

for i in second_input:
    result.append(int(i))

result.sort()

print(result[nth-1])
