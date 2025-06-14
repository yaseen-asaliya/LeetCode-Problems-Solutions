class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = deque()
        c = 0
        prefix = ""
        exists = False

        for x in word:
            if x != ch:
                stack.append(x)
                c+=1
            else:
                stack.append(x)
                exists = True
                break

        if not exists:
            return word

        while(stack):
            prefix+=stack.pop()

        return prefix + word[c+1:]

        