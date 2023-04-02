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
def turn(move,Board):
    new_Board = [[0 for i in range(N)]for j in range(N)]
    #위로 Up 오른쪽 Right 아래 Down 왼쪽 Left
    if move == "up":
        #시계방향 회전
        for i in range(N):
            for j in range(N):
                new_Board[j][N-1-i] = Board[i][j]
        print("newB up",new_Board)
        return new_Board
    
    if move == "down":
        for i in range(N):
            for j in range(N):
                new_Board[N-1-j][i] = Board[i][j]
        print("newB down",new_Board)
        return new_Board

    if move == "left":
        for i in range(N):
            for j in range(N):
                new_Board[i][N-1-j] = Board[i][j]
                
        print("newleft",new_Board)
        return new_Board

turn("left",Board)
turn("up",Board)
turn("down",Board)