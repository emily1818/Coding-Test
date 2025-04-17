import sys 
from collections import Counter

input = sys.stdin.readline

#뒤에 있는 수들의 합을 미리 구해서 곱하기가 떠 빠르다. 

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
result = 0

for i in range(n) :
    total -= arr[i]
    result += arr[i] * total

print(result)