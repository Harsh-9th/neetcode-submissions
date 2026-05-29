
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        saved = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
        
            if sorted_word not in saved:
                saved[sorted_word] = []
        
            saved[sorted_word].append(word)
        
        return list(saved.values())