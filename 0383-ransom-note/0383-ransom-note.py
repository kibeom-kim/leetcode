class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # d = defaultdict(int)

        # for c in magazine: 
        #     d[c] += 1
        
        # for c in ransomNote:
        #     if not d.get(c):
        #         return False
            
        #     d[c] -= 1
        
        # return True
        c_freq = {c: ransomNote.count(c) for c in set(ransomNote)}
        return all(magazine.count(c) >= freq for c, freq in c_freq.items())
