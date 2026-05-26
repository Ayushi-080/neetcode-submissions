class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=defaultdict(list)
        for word in strs:
            ana="".join(sorted(word))
            anagram[ana].append(word)
        return list(anagram.values())