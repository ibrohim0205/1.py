import os
os.system("cls")

def calculate_min_trucks(N, K):
    return (N + K - 1) // K

N = int(input().strip())
K = int(input().strip())

result = calculate_min_trucks(N, K)

print(result)