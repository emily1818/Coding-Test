import sys 
from collections import Counter

input = sys.stdin.readline




ahdma = ["a", "e", "i", "o", "u"]

def start(password) :   
    #모음을 반드시 하나 
    set_password = set(list(password))
    if not any(vowel in password for vowel in ahdma) :
        return print(f"<{password}> is not acceptable.")

    # 모음 3개 혹은 자음 3개가 연속으로 오면 안됨
    #슬라이딩 윈도우 해놓고 모음 개수가 0이거나 3면 out

    for i in range(len(password) - 2):
        window = password[i:i+3]
        cnt = sum(1 for ch in window if ch in ahdma)
        if cnt == 0 or cnt == 3:
            return print(f"<{password}> is not acceptable.")

    # 같은 글자가 연속으로 두번 오면 안되지만, ee랑 oo는 ㄱㅊ음
    for i in range(len(password) - 1):
        if password[i] == password[i+1] and password[i] not in ['e', 'o']:
            return print(f"<{password}> is not acceptable.")
    return print(f"<{password}> is acceptable.")


while True :
    password = input().strip()
    if password == "end" :
        break 
    start(password)
