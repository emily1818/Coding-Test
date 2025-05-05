import sys
input = sys.stdin.readline

n = int(input())
people = []

for _ in range(n):
    weight, height = map(int, input().split())
    people.append((weight, height))

result = []

for i in range(n):
    rank = 1
    for j in range(n):
        if i == j:
            continue
        if people[j][0] > people[i][0] and people[j][1] > people[i][1]:
            rank += 1
    result.append(rank)

print(' '.join(map(str, result)))
