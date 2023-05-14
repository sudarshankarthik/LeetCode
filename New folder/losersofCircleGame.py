def circularGameLosers(self, n: int, k: int) -> list[int]:
    crnt = (1 + 1*k) % n
    visited = [1]
    remaining = [i for i in range(2,n+1)]
    count = 2
    while crnt not in visited:
        visited.append(crnt)
        remaining.pop(remaining.index(crnt))

        crnt = ( crnt + count*k) % n
    return remaining

print(circularGameLosers(0,3,2))