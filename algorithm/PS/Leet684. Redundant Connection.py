from typing import Union


class UnionFind:
    def __init__(self, length) -> None:
        self.__parent = [i for i in range(length)]
    
    def find(self, i):
        if i == self.__parent[i]:
            return i
        self.__parent[i] = self.find(self.__parent[i])
        return self.__parent[i]
    
    def union(self, i, j):
        if i == j:
            return False
        
        p_i = self.find(i)
        p_j = self.find(j)
        if p_i == p_j:
            return False
        
        self.__parent[p_j] = p_i
        return True
    
    def count_disjoint_set(self):
        return len(set([self.find(i) for i in range(len(self.__parent))]))

    def print(self):
        print(self.__parent)

def findRedundantConnection(edges):
    graph = UnionFind(len(edges))
    for _, edge in enumerate(edges):
        if not graph.union(edge[0]-1, edge[1]-1):
            return edge

print(findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))