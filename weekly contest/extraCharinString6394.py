def minExtraChar(self,s: str,dictionary: list[str]) -> int:
	def searchString(i,j):
		leftOut = 0
		for l in range(i,len(s)):
			for r in range(l,len(s)+1):
				subS = s[l:r]
				if subS in d:
					print("sub found", subS)
					leftOut += searchString(r,r)
			print(s[l:r],leftOut)
			leftOut += 1
		return leftOut

	return searchString(0,0)

s = "leetscode"
d = ["leet","code","leetcode"]
print(minExtraChar(0,s,d))