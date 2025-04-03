class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                top = stack[-1]
                if abs(ast) > top:
                    stack.pop()
                    continue
                elif abs(ast) == top:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast)

        return list(stack)