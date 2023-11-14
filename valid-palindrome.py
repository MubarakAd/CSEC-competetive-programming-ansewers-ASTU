class Solution:
    def isPalindrome(self, s: str) -> bool:
        length=len(s)
        output=[]
        for i in range(length):
            if s[i].isalpha() or s[i].isdigit():
                output.append(s[i])
            else:
                continue
        finall=("".join(output))
        finall=finall.lower()
        final2=finall[::-1]
        
        if finall==final2:
            return True
        else:
            return False
