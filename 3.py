import os
os.system("cls")

def find_ways_to_sum(N):
    ways_count = 0
    for i in range(N + 1):
        j = N - i
        if i >= 0 and j >= 0:
            ways_count += 1

    return ways_count


N = int(input("N sonini kiriting: "))
result = find_ways_to_sum(N)
print(f"{N} soni necha xil usulda nomanfiy ikki sonning yig’indisi shaklida yozish mumkinligi: {result}")