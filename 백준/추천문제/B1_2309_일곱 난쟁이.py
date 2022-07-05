from sys import stdin

dwarfs = [int(stdin.readline()) for i in range(9)]

dwarfs.sort()

total = sum(dwarfs)

# 다 더한 키에서 두 명을 더해서 오버된 키가 나오면 그 둘을 제외

flag = False
for i in range(8):
    for j in range(i+1, 9):
        if total - 100 == dwarfs[i]+dwarfs[j]:
            for k in range(9):
                if k != i and k != j:
                    print(dwarfs[k])
            flag = True
            break
    if flag:
        break