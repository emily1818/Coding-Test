import sys

input = sys.stdin.readline

word_arr = input().strip()
stack = []
answer = ""
inside = False

for i in word_arr :
    
    if i == "<" :
        while stack :
            answer += stack.pop()
        answer += i 
        inside = True

    elif i == ">" : 
        answer += i
        inside = False
    #괄호 안에 들어간 경우
    elif inside == True :
        answer += i
    # 띄어쓰기 
    elif i == " ":
        while stack :
            answer += stack.pop()
        answer += " "

    #괄호 안에 안들어간 경우
    # stack에 넣고 거꾸로 출력
    elif inside == False :
        stack.append(i)

if stack : 
    while stack :
        answer += stack.pop()

print(answer)




