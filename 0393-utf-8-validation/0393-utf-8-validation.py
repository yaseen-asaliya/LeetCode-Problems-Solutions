class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0

        for byte in data:
            byte &= 0xFF  

            if remaining == 0:
                mask = 0b10000000
                count = 0

                while mask & byte:
                    count += 1
                    mask >>= 1

                if count == 0:
                    continue  
                if count == 1 or count > 4:
                    return False

                remaining = count - 1
            else:
                if not (byte & 0b10000000 and not (byte & 0b01000000)):
                    return False
                remaining -= 1

        return remaining == 0
