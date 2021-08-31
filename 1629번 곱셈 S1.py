import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a%c
    elif b%2==0:
        return solution(a, b//2, c)**2 % c
    else:
        return (solution(a, b//2, c)**2 * (a%c))%c
print(solution(a,b,c))