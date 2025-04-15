import sys

input = sys.stdin.readline

#대문자 검색
word = input().upper().strip()

# 있는 단어 검색
#리스트로 만들고, set으로 중복 없애기
word_list = list(set(word))

cnt = []

#갯수 세기 
for i in word_list :
    count = word.count
    cnt.append(count(i))
    
if cnt.count(max(cnt)) >1 :
    print("?")
else :
    print(word_list[(cnt.index(max(cnt)))])


