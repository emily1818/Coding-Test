import sys
input = sys.stdin.readline

line = str(input())
#괄호를 쳐서 최소로 만들기

#ㅇㅇ +ㅇㅇ -ㅇㅇ -ㅇㅇ + ㅇㅇ +ㅇㅇ 
#걍 앞에 마이너스 하나 발견되는 순간 +든 - 는 다 빼버리면 되는

arr_plus_minus = []
arr_num = []
num = ""
plus_minus = ""
result = 0 


for n in line :
    if n == "-" :

        if "-" in arr_plus_minus:
            num = int(num) * (-1)
        else :
            num = int(num)

        arr_plus_minus.append(n)
        arr_num.append(num)
        num = ""
        
    elif n == "+" :
        if "-" in arr_plus_minus:
            num = int(num) * (-1)
        else :
            num = int(num)

        arr_num.append(num)
        num = ""

    else :
        num = num + n

#마지막 숫자 
num = int(num)
if "-" in arr_plus_minus:
    num = int(num) * (-1)
else :
    num = int(num)

arr_num.append(num)

for num in arr_num : 
    result = result + num 

print(result)



