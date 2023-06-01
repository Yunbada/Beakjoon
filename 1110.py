#0<=Number<=99 Number가 한자리수면 01,02 이런식으로 바꿔야함
#공식: 십의자리 수 + 일의자리 수 = 결과값, 일의자리수*10 + 결과값의 오른쪽 수
#다시 원래 수로 돌아오는데 걸리는 사이클 수 N 구하기

#입력
num = list(map(int,input()))

#분할 방법
def change(num):
    #입력이 1자리면 수정
    if len(num) == 1:
        temp = num[0]
        num[0] = 0
        num.append(temp)
    tmp = num[0] + num[1]
    tmp2 = tmp%10
    ans =tmp2 + num[1]*10
    ans = list(map(int,str(ans)))
    if len(ans) == 1:
        temp = ans[0]
        ans[0] = 0
        ans.append(temp)
    return ans

ans = change(num)
N = 1
while(1):
    if  ans == num:
        print(N)
        break
    else:
        N+=1
        ans = change(ans)
    
#맞았습니다! 야호~
