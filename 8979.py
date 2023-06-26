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

#병합정렬 알고리즘 생성
def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

#국가의 수 & 몇등인지 입력
c,r = map(int,input().split())
#국가순서대로 금은동 메달 갯수
clist = []
for i in range(c):
    clist.append(list(map(int,input().split())))

#순위 찾기
merge_sort(clist[?][1])
#어캐풀어 이거;