import sys 
from collections import Counter
input = sys.stdin.readline


# 6명의 선수 -> 6명 아니면 탈락
#상위 4명의 주자의 점수를 합하기
# 결승점을 통과한 순서대로 점수 
#점수를 더하여 가장 낮은 점수를 얻는 팀이 승리 -> 동점 -> 5번째 주자
T = int(input())
for _ in range(T) :
    result = 0 
    not_deserve = []
    dict_team = {}
    score= 1

    n = int(input())
    line = list(map(int, input().split()))
    counter = Counter(line)
    # 자격이 없는 팀 제외
    for i in counter :
        if counter[i] >= 6:
            dict_team[i] = []
    
    for i in line :
        if i in dict_team :
            dict_team[i].append(score)
            score += 1

    #점수 계산하기
    min = 10000000
    min_idx = 0 
    for i in dict_team : 
        sum = 0 
        for j in range(4) :
            sum += dict_team[i][j]
        if sum < min :
            min = sum 
            min_idx = i
        elif sum == min :
            if dict_team[i][4] < dict_team[min_idx][4] :
                min_idx =i 
            
        

    print(min_idx)
            

