from sys import stdin
import heapq

test = int(stdin.readline())

for t in range(test):
    k = int(stdin.readline())
    max_heap = []
    min_heap = []
    check = [False] * 1000000
    for i in range(k):
        com = stdin.readline().rstrip().split()

        if com[0] == 'I':
            heapq.heappush(min_heap, (int(com[1]), i))
            heapq.heappush(max_heap, (int(com[1])*-1, i))
            check[i] = True
        elif com[0] == 'D':
            if com[1] == '-1' and min_heap:
                while min_heap and check[min_heap[0][1]]==False:
                    heapq.heappop(min_heap)
                if min_heap:
                    temp = heapq.heappop(min_heap)
                    check[temp[1]] = False
            elif com[1] == '1' and max_heap:
                while max_heap and check[max_heap[0][1]]==False:
                    heapq.heappop(max_heap)
                if max_heap:
                    temp = heapq.heappop(max_heap)
                    check[temp[1]] = False
    
    while max_heap and check[max_heap[0][1]]==False:
        heapq.heappop(max_heap)
    while min_heap and check[min_heap[0][1]]==False:
        heapq.heappop(min_heap)
    if max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
                    