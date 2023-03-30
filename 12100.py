#2048 게임
#첫줄에 보드의 크기 N(1<= N <=20), N X N 크기의 보드판
#둘째 줄부터 초기의 상태 (0은 빈공간, 블록에 씌여이쓴ㄴ 수는 2보다 크거나 같고 1024보다 작거나 같은 2의 제곱꼴)
#최대 5번 이동시켜서 얻으 수 이쓴 가장 큰 블록 출력

#보드 설정
N = int(input())
Board = [[0 for i in range(N)]for J in range(N)]
Num = []

for i in range(N):
    Num.append(list(map(int, input().split())))

#