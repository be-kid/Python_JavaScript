#nCr = n!/(n-r)!r!

from sys import stdin

n, r = map(int,stdin.readline().split())

fact = [0 for i in range(101)]

fact[0] = 1
fact[1] = 1

for i in range(2, 101):
    fact[i] = fact[i-1]*i

print(fact[n]//(fact[n-r]*fact[r]))