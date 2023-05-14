self = 0
str = 'babad'

def longestPalindrome(self,s: str) -> str:
    lonSubStr = s[0]
    lenlonSubStr = 1
    lenStr = len(s)

    for i in range(lenStr):
        if(i+lenlonSubStr) > lenStr:
            break
        str = s[i:i+lenlonSubStr-1]
        for j in range(i+lenlonSubStr-1,lenStr):
            str += s[j]
            print(str)
            if str == str[::-1]:
                if len(str) > lenlonSubStr:
                    lenlonSubStr = len(str)
                    lonSubStr = str
        print()
    return lonSubStr
print(longestPalindrome(self,str))