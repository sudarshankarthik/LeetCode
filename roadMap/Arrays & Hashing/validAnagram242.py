def isAnagram(self,s: str,t: str) -> bool:
    if(len(s) != len(t)):
        return False
    return sorted(tuple(s)) == sorted(tuple(t))

s = "aabb"
t = "bbaa"

print(isAnagram(0,s,t))