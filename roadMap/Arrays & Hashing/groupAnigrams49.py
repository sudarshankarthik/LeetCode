
def groupAnagrams(self,strs: list[str]) -> list[list[str]]:
    anagrams = {}
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for s in strs:
        t = []
        for c in range(26):
            if  alphabets[c] in s and alphabets[c] not in t:
                t.append((alphabets[c], s.count(alphabets[c])))
        t = tuple(t)
        if t in anagrams:
            anagrams[t].append(s)
        else:
            anagrams[t] = [s]
    return anagrams.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(0,strs))