import sys

input = sys.stdin.readline

n, m = map(int, input().split())

not_hear = set()
not_see_hear = []

# 듣도 못한 사람들을 집합으로 저장
for _ in range(n):
    not_hear.add(input().strip())

# 보지도 못한 사람 중, 듣도 못한 사람 판별
for _ in range(m):
    not_see = input().strip()
    if not_see in not_hear:  # ✅ O(1) 탐색
        not_see_hear.append(not_see)

# 사전순 정렬 후 출력
not_see_hear.sort()

print(len(not_see_hear))
for name in not_see_hear:
    print(name)
