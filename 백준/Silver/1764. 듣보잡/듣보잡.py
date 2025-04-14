import sys
input = sys.stdin.readline

N, M = map(int, input().split())

not_heard = []
not_seen = []
cnt = 0 
not_heard_seen = []

for i in range(N) :
    name = input()
    # print(name)
    not_heard.append(name)

for i in range(M) : 
    name = input()
    not_seen.append(name)

#각 arr를 set으로 풀어주고 &연산자를 통해 교집합 부분만 빼서 list로 만들고 출력
not_heard_seen = list(set(not_heard) & set(not_seen))
#시간 초과 남..;;
# for name in not_heard : 
#     if name in not_seen :
#         cnt +=1 
#         not_heard_seen.append(name)

not_heard_seen.sort()

# print(not_heard[0])
print(len(not_heard_seen))

# for name in not_heard_seen :
#     print(name)

print("".join(not_heard_seen), end = "")