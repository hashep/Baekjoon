normal_chess_set = [1, 1, 2, 2, 2, 8]

current_chess_set = list(map(int, input().split()))

for i in range(6):
    print(normal_chess_set[i] - current_chess_set[i], end=" ")