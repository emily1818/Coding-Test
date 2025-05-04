import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    level, name = input().split()
    level = int(level)

    placed = False
    for room in rooms:
        room_level = room[0][0]  # 기준 레벨
        if len(room) < m and room_level - 10 <= level <= room_level + 10:
            room.append((level, name))
            placed = True
            break

    if not placed:
        rooms.append([(level, name)])  # 새 방 생성

# 출력
for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    for player in sorted(room, key=lambda x: x[1]):
        print(player[0], player[1])
