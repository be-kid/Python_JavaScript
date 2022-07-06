"""
ex)
[3, 1] -> 0: 75%, 1: 25%
[5, 3, 2] -> 0: 50%, 1: 30%, 2: 20%
"""

"""
random function ex)
random.randrange(stop)
  -> integer uniform random distribution of 0 <= x < stop
random.randrange(start, stop)
  -> integer uniform random distribution of start <= x < stop
random.random()
  -> float uniform random distribution of 0 <= x < 1
random.uniform(a, b)
  -> float uniform random distribution of a <= x <= b
"""

import random

def weighted_random(weights: list[int]) -> int:
    total = sum(weights)

    w = []
    for i in range(len(weights)):
        w.append(weights[i] / total)
    
    for i in range(1, len(weights)):
        w[i] = w[i-1]+w[i]

    # 여기까지는 어쩔수 없음

    random_num = random.random()

    start = 0
    end = len(w)-1
    mid = 0

    #print(w)
    #print(random_num)
    #random_num = 0.7
    while start < end:
        mid = (start+end) // 2
        #rint(start, mid, end)
        if random_num >= w[mid]:
            start = mid + 1
        else:
            end = mid
    
    return end
        

result = [0, 0, 0, 0, 0]
for i in range(100000):
    result[weighted_random([1, 3, 2, 4])] += 1

print(result)