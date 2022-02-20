from sys import stdin
import math

a, b, v = map(int, stdin.readline().split())

print(math.ceil((v-a)/(a-b))+1)