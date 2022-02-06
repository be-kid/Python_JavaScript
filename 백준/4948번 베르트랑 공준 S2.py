from sys import stdin

nums = [True for i in range(123456*2 + 1)]


idx = 2;
while idx <= 123456:
    for i in range(idx*2, 123456*2+1, idx):
        nums[i] = False
    idx+=1;
    while nums[idx] != True:
        idx+=1
        
result = [0 for i in range(123456*2+1)]

for i in range(2, len(nums)):
    if nums[i] == True:
        result[i] = result[i-1]+1
    else:
        result[i] = result[i-1]

while True:
    n = int(stdin.readline())
    if n==0:
        break
    print(result[2*n] - result[n])