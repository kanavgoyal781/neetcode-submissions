class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(left,right,s):
            while left<right:
                if s[left]==s[right]:
                    left=left+1
                    right=right-1
                else:
                    return False
            return True
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i=i+1
                j=j-1
            else:
                return is_pal(i+1,j,s) or is_pal(i,j-1,s)
        return True