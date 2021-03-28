def findSmallestSetOfVertices(n: int, edges):
    output = set(range(0, n))
    print(output)
    for edge in edges:
        if edge[1] in output:
            output.remove(edge[1])

    return list(output)

def findSmallestSetOfVertices2(n: int, edges):
    output = [0]*n
    
    for edge in edges:
        output[edge[1]] = 1

    return [ix for ix, val in enumerate(output) if val is 0]

print(findSmallestSetOfVertices2(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))