class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(list(s)) == sorted(list(t)) and len(sorted(list(s))) == len(sorted(list(t))):
         return True
        else:
         return False