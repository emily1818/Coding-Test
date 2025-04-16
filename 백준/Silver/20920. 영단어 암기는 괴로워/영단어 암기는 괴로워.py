import sys 
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n) :
    s = input().strip()
    if len(s) >= m : 
        arr.append(s)

counter_arr = Counter(arr)

counter_arr = sorted(counter_arr.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수


for i in range(len(counter_arr)) :
    word, fre = counter_arr[i]
    print(word)