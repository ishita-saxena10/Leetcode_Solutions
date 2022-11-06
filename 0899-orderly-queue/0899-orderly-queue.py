class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        answer=s
        if k==1:
            for i in range(len(s)):
                answer=min(answer,s[i:] + s[:i])
            return answer
        return "".join(sorted(s))