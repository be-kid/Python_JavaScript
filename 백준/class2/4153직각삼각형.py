from sys import stdin

while True:
    nums = list(map(lambda x: int(x)*int(x), stdin.readline().split()))
    total = sum(nums)
    if total==0:
        break
    
    if total-max(nums)*2==0:
        print("right")
    else:
        print("wrong")