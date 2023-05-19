def isBipartite(self,graph: list[list[int]]) -> bool:
    set = [0 for i in range(len(graph))]
    def checkBiparte(node: int,chk = 1):
        flag = False
        if set[node] == 0:
            set[node] = chk
            flag = True
        crntNode = set[node]
        for i in range(len(graph[node])):
            chckNode = set[graph[node][i]]

            if chckNode == 0:
                set[graph[node][i]] = crntNode * -1
            elif crntNode * chckNode == -1:
                continue
            elif chk == 1:
                checkBiparte(graph[node][i], -crntNode)
            else:
                return False
        return True

    for i in range(len(graph)):
        if checkBiparte(i):
            continue
        else:
            return False
    return True

print(isBipartite(0,[[1],[0,3],[3],[1,2]]))
