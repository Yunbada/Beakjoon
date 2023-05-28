#2048 게임
#첫줄에 보드의 크기 N(1<= N <=20), N X N 크기의 보드판
#둘째 줄부터 초기의 상태 (0은 빈공간, 블록에 씌여이쓴ㄴ 수는 2보다 크거나 같고 1024보다 작거나 같은 2의 제곱꼴)
#최대 5번 이동시켜서 얻으 수 이쓴 가장 큰 블록 출력

#보드 설정
N = int(input())
Board = []


for i in range(N):
    Board.append(list(map(int, input().split())))

#배열의 특징? 오른쪽으로 이동하려함 꺾어서 사용하자?
#오른쪽으로 합친다.
def turn(move,Board):
    new_Board = [[0 for i in range(N)]for j in range(N)]
    #위로 Up 오른쪽 Right 아래 Down 왼쪽 Left
    if move == "up":
        #시계방향 회전
        for i in range(N):
            for j in range(N):
                new_Board[j][N-1-i] = Board[i][j]
        print("newup",new_Board)
        return new_Board
    #반시계방향
    if move == "down":
        for i in range(N):
            for j in range(N):
                new_Board[N-1-j][i] = Board[i][j]
        print("newdown",new_Board)
        return new_Board
    #가운데를 기준으로 회전
    if move == "left":
        for i in range(N):
            for j in range(N):
                new_Board[i][N-1-j] = Board[i][j]     
        print("newleft",new_Board)
        return new_Board

#보드전부 합치기
def sum(Board):
    Board2 = [[0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            #배열에서 같은 같은 행에서 숫자 찾기
            #먼저 숫자를 오른쪽으로 이동
            if Board[i][N-1-j] == 0:
                    if Board[i][N-2-j] == 0:
                        j= j+1
                        return Board2
                    else:
                        Board2[i][N-1-j] = Board[i][N-2-j]
                        j = 0
                        return Board2
            else:
                Board2 = Board[i][N-1-j]
                return Board2
        #숫자 비교후 합치기
    for k in range(N):
            if Board2[i][N-1-k] == Board2[i][N-2-k]:
                Board[i][N-1-k] = Board2[i][N-1-k]*2
                Board2[i][N-1-k] =Board2[i][N-1-k]*2
                Board2[i][N-2-k] = 0
                return Board
            else:
                Board2[i][N-1-k] = Board2[i][N-2-k]
                Board[i][N-1-k] = Board2[i][N-2-k]
                Board2[i][N-2-k] = 0
                return Board
                
            
            
                
                
                
                
                    
Board = sum(Board)
print(Board)

