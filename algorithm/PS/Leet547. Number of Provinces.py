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
            return
        
        p_i = self.find(i)
        p_j = self.find(j)
        print("p:",p_i, p_j)
        if p_i == p_j:
            return
        
        self.__parent[p_j] = p_i
    
    def count_disjoint_set(self):
        return len(set([self.find(i) for i in range(len(self.__parent))]))

    def print(self):
        print(self.__parent)


def findCircleNum(isConnected):
    union_find = UnionFind(len(isConnected))
    for i in range(len(isConnected)):
        for j in range(i+1, len(isConnected)):
            print(i, j, isConnected[i][j])
            if isConnected[i][j] == 1:
                union_find.union(i, j)
                union_find.print()

    union_find.print()
    print(union_find.count_disjoint_set())

if __name__ == '__main__':
    findCircleNum([[1,1,0],[1,1,0],[0,0,1]])