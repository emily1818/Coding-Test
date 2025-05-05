#구르밍 떠 있이면 0, 몇분후에 처음으로 구름이 뜨는지
# 구름이 영영 안뜨면 0 

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = [[-1] * w for _ in range(h)]

for i in range(h) :
    cloud_exist = False
    line = list(map(str, input().strip()))
    for idx, j in enumerate(line) :
        if cloud_exist :
            cnt += 1
            arr[i][idx] = cnt
        if j == "c" :
            arr[i][idx] = 0 
            cloud_exist = True
            cnt = 0

for i in arr :
    print(" ".join(map(str, i)))