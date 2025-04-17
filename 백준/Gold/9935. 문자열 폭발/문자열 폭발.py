import sys
input = sys.stdin.readline

s = input().strip()
bomb = input().strip()
len_bomb = len(bomb)

stack = []

for char in s:
    stack.append(char)
    # 폭탄 길이만큼 비교
    if len(stack) >= len_bomb:
        if ''.join(stack[-len_bomb:]) == bomb:
            for _ in range(len_bomb):
                stack.pop()

result = ''.join(stack)
print(result if result else "FRULA")
