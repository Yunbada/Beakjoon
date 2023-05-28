#소수&팰린드롬
#어떤 수와 그 수의 숫자 순서를 뒤집은 수가 일치하는 수를 팰린드롬이라 부름 
#예로 79197과 324423 등이 팰린드롬 수이다.
#1<= N <= 1000000, N보다 크거나 같고, 소수이면서 팰린드롬인 수중 가장 작은수
import math

def findPN(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i == 0:
            return 0
    return num

def revers(num):
    num_list = list(map(int,str(num)))
    num_listr = list(reversed(num_list))
    if num_list != num_listr:
        return 0
    return num


n = int(input())

while True:
    #N보다 큰 소수 찾기
    if n == 1:
        print("2")
        break
    elif findPN(n) == 0 or revers(n) == 0:
        n+=1
        continue
    else:
        print(n)
        break
    
#정답입니다! 얏호~