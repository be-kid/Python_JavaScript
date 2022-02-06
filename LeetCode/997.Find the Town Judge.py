class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        check = [0 for i in range(n+1)]
        g = {}
        for i in range(1, n+1):
            g[i] = []
        for i in trust:
            g[i[0]].append(i[1])
        
            check[i[1]] += 1
        
        for i in range(1, n+1):
            if check[i] == n-1 and len(g[i]) == 0:
                return i
        return -1
    
'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
'''