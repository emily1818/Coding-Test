import sys

input = sys.stdin.readline

n = int(input())
dict_name = {}
for _ in range(n) :
    file_name, file_expert =input().strip().split(".")
    if file_expert in dict_name :
        dict_name[file_expert] +=1
    else :
        dict_name[file_expert] = 1 

for ext in sorted(dict_name) :
    print(ext, dict_name[ext])