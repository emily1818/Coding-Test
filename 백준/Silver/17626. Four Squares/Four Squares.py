import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

for i in range(1, n + 1):
    # 일단 최댓값으로 초기화 (모두 1^2로 더하는 경우)
    dp[i] = i
    for j in range(1, int(i ** 0.5) + 1):
        square = j * j
        if square > i:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[n])
