class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            counts = [0]*26
            for c in word:
                counts[ord(c) - ord('a')] += 1
            key = tuple(counts)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())

