import sys 
input = sys.stdin.readline

n = int(input())
score_1 = 0 
score_2 =0 
winning_1 = 0 
winning_2 = 0 
start = 0 
end = 0 
winning_team = 0 
gg = 0 

def time_to_sec(t) :
    m, s = map(int, t.split(":"))
    return m * 60 + s

def sec_to_time(t) :
    m = t//60
    s = t%60
    return f"{m:02}:{s:02}"

for _ in range(n) :
    num, time = map(str, input().split())
    #승점 
    num = int(num)
    if num == 1 :
        score_1 += 1
    else :
        score_2 += 1

    #start 갱신을 언제 해야할 할까 -> 다른 팀이 이겼을 때 현재의 winning team이 지금의 team일때 
    # 1이 이기고 있는데 1이 점수 땀 x
    # 비기고 그다음에 점수 땀 이때 갱신 

    if score_1 != score_2 :
        # start = time 
        if gg == 0  :
            start = time 
        gg = 1
        if score_1 > score_2 :
            winning_team = 1
        else :
            winning_team = 2

    else :
        gg = 0 
        end = time
        winning_time = time_to_sec(end)-time_to_sec(start)
        if winning_team ==1 :
            winning_1 += winning_time
            winning_team = 0 
        elif winning_team == 2 :
            winning_2 += winning_time
            winning_team = 0 

winning_time = time_to_sec("48:00")-time_to_sec(start)
if winning_team ==1 :
    winning_1 += winning_time
elif winning_team == 2:
    winning_2 += winning_time

print(sec_to_time(winning_1))
print(sec_to_time(winning_2))




