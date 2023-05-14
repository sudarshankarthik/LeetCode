def mostPoints(self,questions: list[list[int]]) -> int:
    lenQns = len(questions)
    dp = {}
    def res(i):
        if(i >= lenQns):
            return 0
        if i in dp:
            return dp[i]
        dp[i] = max(res(i+1),(questions[i][0]+res(i+1+questions[i][1])))
        return dp[i]
    return res(0)

qns = [[1,1],[2,2],[3,3],[4,4],[5,5]]
print(mostPoints(1,qns))