class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        length = len(s)

        if length != len(t):
            return False
        
        for i in range(length):
            map1[s[i]] += 1
            map2[t[i]] += 1

        return map1 == map2