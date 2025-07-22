class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def is_match(p, w):
            if len(p) == 0:
                return True
            if len(w) == 0 or p[0] != w[0]:
                return False
            return is_match(p[1:], w[1:])
        
        def is_substring(p, w):
            if len(w) < len(p):
                return False
            if is_match(p, w):
                return True
            return is_substring(p, w[1:])  
        
        def count(patterns, i):
            if i == len(patterns):
                return 0
            match = 1 if is_substring(patterns[i], word) else 0
            return match + count(patterns, i + 1)
        
        return count(patterns, 0)