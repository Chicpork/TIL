def findCenter(edges):
    return set(edges[0]).intersection(set(edges[1])).pop()

print(findCenter([[1,2],[2,3],[4,2]]))