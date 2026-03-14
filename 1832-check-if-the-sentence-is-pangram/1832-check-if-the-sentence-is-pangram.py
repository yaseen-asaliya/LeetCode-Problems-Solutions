class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        temp = set()

        for x in sentence:
            temp.add(x)

        return True if len(temp) == 26 else False