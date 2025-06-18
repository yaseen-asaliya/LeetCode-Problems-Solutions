class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        freq = {}
        res = []
        st = s1 + " " + s2

        for word in st.split(' '):
            if not word in freq:
                freq[word] = 1
            else:
                freq[word] += 1
        
        for key, val in freq.items():
            if val == 1:
                res.append(key)

        return res