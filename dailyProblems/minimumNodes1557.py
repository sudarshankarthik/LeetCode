def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    out = [i for i in range(n)]
    for i in edges:
        out[i[1]] = -1

    out = filter(lambda x:x != -1,out)
        
    return list(out)