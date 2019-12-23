def todigit(num):
    digit=0
    for i in str(num):
        digit+=int(i)
    
    if digit<10:
        print(digit)
    else:
        todigit(digit)



while(True):
    text=input()
    if text=='0':
        break

    todigit(text)