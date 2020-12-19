def check_left(wheel,check_num, rotate_dir):
    if check_num-1<0:
        return
    
    if wheel[check_num-1][2] == wheel[check_num][6]:
        return

    check_left(wheel,check_num-1,not rotate_dir)
    rotate(wheel[check_num-1],not rotate_dir)


def check_right(wheel,check_num, rotate_dir):
    if check_num+1>3:
        return
    
    if wheel[check_num+1][6] == wheel[check_num][2]:
        return

    check_right(wheel,check_num+1,not rotate_dir)
    rotate(wheel[check_num+1],not rotate_dir)




def rotate(rotate_wheel, rotate_dir):
    # -1 이면 반시계 방향으로 회전
    if(rotate_dir == False):
        tmp = rotate_wheel.pop(0)
        rotate_wheel.append(tmp)
    
    # 0 이면 시계 방향으로 회전
    else:
        tmp = rotate_wheel.pop()
        rotate_wheel.insert(0, tmp)



# 톱바퀴 입력 받기
wheel = []

for i in range(4):
    tmp_wheel = list(map(int,input()))
    wheel.append(tmp_wheel)



loop_count = int(input())


for i in range(loop_count):
    # 입력
    rotate_wheel_num, rotate_dir = map(int, input().split())
    rotate_wheel_num-=1
    if rotate_dir ==1:
        rotate_dir = True
    else:
        rotate_dir = False

    # 왼쪽 체크
    check_left(wheel,rotate_wheel_num,rotate_dir)

    # 오른쪽 체크
    check_right(wheel,rotate_wheel_num,rotate_dir)

    # 본인꺼 회전
    rotate(wheel[rotate_wheel_num],rotate_dir)


# 점수계산
answer = 0
num=1
for i in wheel:
    if i[0] == 1:
        answer+=num
    num*=2

print(answer)

    

