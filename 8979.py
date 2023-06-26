#8979 올림픽
#금,은,동 규칙에 따른 순위
#1. 금메달 수가 많은 곳
#2. 은메달수가 더 많은곳
#3. 동메달 수가 더 많은 곳
#입력 예제
#4 3 (국가의 수, 국가 번호의 등수)
#1 1 2 0
#2 0 1 0
#3 0 1 0
#4 0 0 1
#출력 예제
#2

#국가의 수 & 국가 번호 입력
c,r = map(int,input().split())
#국가순서대로 금은동 메달 갯수
clist = []
for i in range(c):
    clist.append(list(map(int,input().split())))

#순위 찾기
clist.sort(key = lambda x:(-x[1],-x[2],-x[3]))
rank = 1
#print(clist)
for i in range(c):
    if clist[i][0] == r:
        r = i
        break
    
for i in range(c):
    if i != r:
        if clist[i][1] > clist[r][1]:
            rank += 1
        elif clist[i][1] == clist[r][1]:
            if clist[i][2] > clist[r][2]:
                rank += 1
            elif clist[i][2] == clist[r][2]:
                if clist[i][3] > clist[r][3]:
                    rank += 1
print(rank)

#정답입니다 얏호~