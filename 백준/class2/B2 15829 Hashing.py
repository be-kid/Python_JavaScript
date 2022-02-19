from sys import stdin
L = int(stdin.readline())
string = stdin.readline()

mod = 1234567891

result = 0
for i in range(L):
    result += (ord(string[i])-96)*(pow(31, i)%mod)
    result %= mod
print(result)