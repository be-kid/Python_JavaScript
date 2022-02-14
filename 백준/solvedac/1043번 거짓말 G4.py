from sys import stdin

n, m = map(int, stdin.readline().split())
true_man = set(list(map(int, stdin.readline().split()))[1:])

party = []

for i in range(m):
    party.append(list(map(int, stdin.readline().split()))[1:])

while True:
    count = 0
    tmp = party
    for x in tmp:
        if true_man & set(x):
            true_man.update(x)
            party.remove(x)
            count+=1
    if count == 0:
        break
print(len(party))




'''
진실을 아는 사람이 있다-> 진실만 말한다
진실을 들은 사람이 다른 파티에서 거짓을 들으면 들통난다

일단 진실만 말해야하는 파티를 모두 걸러내야한다
처음 진실을 아는 사람이 포함된 파티와 그 파티에 포함된 사람들이 포함된 모든 파티를 제거
완전히 관련없는 사람들만 남을 때까지
'''