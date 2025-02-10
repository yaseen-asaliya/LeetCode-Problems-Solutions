class Solution(object):
    def is_digit(self, char):
        return 48 <= ord(char) <= 57

    def clearDigits(self, s):
        stack = []
    
        for char in s:
            if self.is_digit(char):
                while stack and self.is_digit(stack[-1]):
                    stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)

            