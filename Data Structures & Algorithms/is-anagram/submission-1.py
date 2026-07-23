class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if set(sorted(list(s))) == set(sorted(list(t))) and len(set(sorted(list(s)))) == len(set(sorted(list(t)))):
         return True
        else:
         return False