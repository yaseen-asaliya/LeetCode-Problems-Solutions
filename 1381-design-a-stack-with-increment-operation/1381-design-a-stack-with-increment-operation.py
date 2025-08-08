class CustomStack:
    def __init__(self, maxSize: int):
        self.st = []
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.st) < self.maxSize:
            self.st.append(x)

    def pop(self) -> int:
        if not self.st:
            return -1
        return self.st.pop()

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.st))
        for i in range(limit):
            self.st[i] += val



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)