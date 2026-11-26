class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        srez = s[0:k]
        return " ".join(srez)
