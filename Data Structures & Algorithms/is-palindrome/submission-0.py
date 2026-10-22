class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        cleaned = "".join(char for char in s if      char.isalnum()).lower()
        j=len(cleaned)-1
        print(cleaned)
        for i in range(len(cleaned)//2):
            if cleaned[i]!=cleaned[j-i]:
                return False
        return True
            
        