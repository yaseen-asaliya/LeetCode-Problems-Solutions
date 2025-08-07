class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_once = set()
        words1_more = set()
        words2_once = set()
        words2_more = set()

        for word in words1:
            if word in words1_once:
                words1_once.remove(word)
                words1_more.add(word)
            elif word not in words1_more:
                words1_once.add(word)

        for word in words2:
            if word in words2_once:
                words2_once.remove(word)
                words2_more.add(word)
            elif word not in words2_more:
                words2_once.add(word)

        count = 0
        for word in words1_once:
            if word in words2_once:
                count += 1

        return count