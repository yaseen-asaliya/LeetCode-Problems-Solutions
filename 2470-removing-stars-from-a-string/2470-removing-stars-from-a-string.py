class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()


        for st in s:
            if st == '*':
                stack.pop()
            else:
                stack.append(st)

        return "".join(stack)