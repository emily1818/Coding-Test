import sys
input = sys.stdin.readline

n = int(input())


arr = list(map(int, input().split()))
#중복값 제거 + 정렬
sorted_arr = sorted(set(arr))
dic = {}
index = 0 
result_arr = []

for i in sorted_arr :
    dic[i] = index 
    index += 1


for i in arr :
    result_arr.append(dic[i])

    
print(' '.join(map(str, result_arr)))

# print(' '.join(str(result_arr[x]) for x in arr))