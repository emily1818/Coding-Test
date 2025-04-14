import sys
input = sys.stdin.readline



def start(t) :
    dic = {}
    result = 1
    for _ in range(t) :
        kind, body = map(str, input().split())
        if body in dic : 
            dic[body].append(kind)
        else : 
            dic[body] = [kind]

    for items in dic.values() :
        result *= len(items) + 1
    print(result-1)

n = int(input())
for _ in range(n) : 
    
    t = int(input())
    start(t)