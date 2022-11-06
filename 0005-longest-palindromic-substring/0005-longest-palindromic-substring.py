class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(l:int,r:int,s:str):
            while(l>=0 and r< len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        i = 0 
        res = ''
        for i in range(len(s)):
            res1 = palindrome(i,i,s)
            res2 = palindrome(i,i+1,s)
            if len(res1) >len(res):
                res = res1
            if len(res2) > len(res):
                res = res2
        return res