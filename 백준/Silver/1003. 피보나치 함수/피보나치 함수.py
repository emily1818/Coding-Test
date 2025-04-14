import sys
input = sys.stdin.readline

T = int(input())



for _ in range(T) :
    a, b= 0, 1  #1, 0불린 횟수 
    n = int(input())
    if n == 0 :
        print("1", "0")
    else : 
        for i in range(1, n) :
            a, b= b, a+b
        print(a, b)
    



# 시간초과
# def fibonacci(n) : 
#     if n ==0 :
#         return 0
#     elif n==1 :
#         return 1
#     else :
#         return fibonacci(n-1) + fibonacci(n-2)


# for _ in range(T) :
#     n = int(input())
#     print(fibonacci(n-1), fibonacci(n))