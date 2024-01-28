import os
os.system("cls")

def find_forgotten_passenger(N, routes, M):
    total_passengers = 0
    for i in range(N - 1):
        total_passengers += routes[i][1]

    return max(0, total_passengers - M)

N = int(input())
routes = [list(map(int, input().split())) for _ in range(N - 1)]
M = int(input())

result = find_forgotten_passenger(N, routes, M)
print(result)