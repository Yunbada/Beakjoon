#1<=N<=100 방의 크기가 주어지고 몸을 쭉 펴서 누움, 2칸이상 사용함

n = int(input())
#2차원 배열 제작
room = [list(input()) for i in range(n)]
#5
#..X.. 
#X.X.. 
#.XX.X
#..X.X
#X....

#수평 자리 구하기
def horizon(room):
    cnt = 0
    tcnt = 0
    for i in range(n):
        for j in range(n):
            if room[i][j] == ".":
                cnt += 1
            else:
                if cnt >= 2:
                    tcnt += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt >= 2:
            tcnt += 1
            cnt = 0
        else:
            cnt = 0
    return tcnt
            
def turn90(room):
    troom = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            troom[j][n-1-i] = room[i][j]
    return troom


print(horizon(room),horizon(turn90(room)))

#정답입니다! 얏호~
    
    