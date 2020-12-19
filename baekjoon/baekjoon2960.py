# 소수 판별기
def isPrime(num):
    if num == 2:
        return True
    
    if num == 1:
        return False
    
    if num % 2 == 0:
        return False

    for i in range(3,num):
        if num % i == 0:
            return False
    
    return True



def solution():
    n, k = map(int,input().split())

    numbers = []

    remove_count = 0

    # 2 ~ n 까지 모든 수 넣기
    for i in range(2,n+1):
        numbers.append(i)


    while len(numbers)!=0:
        # 최소값 찾기
        min_num = min(numbers)
        min_num_idx = numbers.index(min_num)

        if isPrime(min_num) == False:
            for i in range(min_num_idx+1, len(numbers)):
                if isPrime(numbers[i]) == True:
                    min_num = numbers[i]
                    min_num_idx = i
                    break



        # 최소값 제거
        remove_count+=1
        numbers.remove(min_num)

        if remove_count == k:
                print(min_num)
                return


        need_to_remove = []

        # min num 의 배수 찾기
        for i in range(min_num_idx, len(numbers)):
            if numbers[i] % min_num == 0:
                need_to_remove.append(numbers[i])

        # 제거할 것들 제거하기
        for i in need_to_remove:
            remove_count+=1

            if remove_count == k:
                print(i)
                return
            
            numbers.remove(i)


solution()

            
        