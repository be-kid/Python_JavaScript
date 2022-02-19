from sys import stdin

while True:
    num = stdin.readline().rstrip()
    if num == '0':
        break
    
    if num == num[::-1]:
        print("yes")
    else:
        print("no")