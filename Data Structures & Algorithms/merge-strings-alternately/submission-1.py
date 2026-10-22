class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=''
        p1=0
        p2=0
        for i in range(min(len(word1),len(word2))):
            word3=word3+word1[i]+word2[i]
        return word3+word1[i+1:]+word2[i+1:]
