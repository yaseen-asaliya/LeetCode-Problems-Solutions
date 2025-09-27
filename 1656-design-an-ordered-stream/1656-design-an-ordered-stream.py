
class OrderedStream:
    def __init__(self, n: int):
        self.res = [""] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.res[idKey - 1] = value

        chunk = []
        while self.ptr < len(self.res) and self.res[self.ptr] != "":
            chunk.append(self.res[self.ptr])
            self.ptr += 1   

        return chunk
