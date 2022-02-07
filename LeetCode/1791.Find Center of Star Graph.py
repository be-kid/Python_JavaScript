class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = [0 for i in range(0, len(edges)+1)]
        for edge in edges:
            g[edge[0]-1]+=1
            g[edge[1]-1]+=1
        return g.index(max(g))+1
    

'''
There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
'''