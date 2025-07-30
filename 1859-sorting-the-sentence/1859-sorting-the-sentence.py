class Solution:
    def sortSentence(self, s: str) -> str:
        sentances = s.split(" ")
        res = [""] * len(sentances)

        for sent in sentances:
            index = int(sent[-1])
            res[index-1] = sent[:-1]
        
        return ' '.join(res)
