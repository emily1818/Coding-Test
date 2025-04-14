import sys
input = sys.stdin.readline

N, M = map(int, input().split())
#dictionary로
add = {}

for _ in  range (N) :
    site, id = input().split()
    add[site]  = id

for _ in range(M) :
    print(add[input().strip()])

