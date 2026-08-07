class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for c in s:
                i = ord(c) - ord('a')
                key[i] += 1
            a[tuple(key)].append(s)
        
        return list(a.values())