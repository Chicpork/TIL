def allPathsSourceTarget(graph):
    output = []
    if len(graph[0]) == 0:
        return []
    
    # for ix in graph[0]:
    #     test(graph, ix, [0], output)
    
    test(graph, 0, [], output)
    
    return output

def test(graph, cur, path, output):
    if cur == len(graph)-1:
        output.append(path+[cur])
    
    if len(graph[cur]) == 0:
        return
    
    for ix in graph[cur]:
        test(graph, ix, path + [cur], output)
    


graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(allPathsSourceTarget(graph))