class Solution:
    def number_to_char_array(self, num):
        return list(str(num))

    def compress(self, chars: List[str]) -> int:
        c = 1
        res = []

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                c += 1
            else:
                res.append(chars[i - 1])
                if c > 1:
                    res.extend(self.number_to_char_array(c))
                c = 1

        res.append(chars[-1])
        if c > 1:
            res.extend(self.number_to_char_array(c))

        chars[:] = res
        return len(chars)