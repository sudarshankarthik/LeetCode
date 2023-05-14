self = 0
s = "abcababcdabcabcde"

def lengthOfLongestSubstring(self,s: str) -> int:
    long_len = 0
    i,j = 0,0
    for i in range(len(s)):
        print()
        string = ''
        crnt_len = 0
        for j in range(i,len(s)):
            if s[j] in string:
                break
            string += s[j]
            print(string)
        if(long_len < len(string)):
            long_len = len(string)

    return long_len

print(lengthOfLongestSubstring(self,s))