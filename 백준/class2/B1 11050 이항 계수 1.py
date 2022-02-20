from math import factorial
from sys import stdin

n, k = map(int, stdin.readline().split())

fact = [1 for i in range(11)]
for i in range(1, 11):
    fact[i] = fact[i-1]*i

# n! / k!(n-k)!
print(fact[n]//(fact[k]*fact[n-k]))