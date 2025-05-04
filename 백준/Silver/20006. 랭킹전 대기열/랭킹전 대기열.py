import sys 

input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p) :

    i, n = map(str, input().split())
    i = int(i)

    placed = False  
    for room in rooms : 
        room_level = room[0][0]
        
        if len(room) < m  and int(i) <= room_level+10 and int(i)>= room_level-10 :
            room.append((i, n))
            placed = True 
            break 
        
    if placed == False : 
        rooms.append([(i, n)])

for room in rooms :
    if len(room) == m :
        print("Started!")
       
    else :
        print("Waiting!")

    for player in sorted(room, key=lambda x: x[1]):
        print(player[0], player[1])


