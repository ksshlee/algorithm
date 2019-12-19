score=0
end=False

for i in range(10):
    num=int(input())

    if end == True:
        continue

    if abs(score+num-100)<abs(score-100):
        score+=num
    elif abs(score+num-100)==abs(score-100):
        if score+num>score:
            score+=num
            end=True
        else:
            end=True
    else:
        end=True

print(score)
