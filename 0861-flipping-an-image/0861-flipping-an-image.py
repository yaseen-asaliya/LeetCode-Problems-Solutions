from typing import List

class Solution:
    def invert(self, num: int) -> int:
        return 0 if num else 1 

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)  

        for index in range(n):
            p1 = 0
            for p2 in range(n - 1, n // 2 - 1, -1):  
                image[index][p1], image[index][p2] = image[index][p2], image[index][p1]
                p1 += 1
            
        for index in range(n):
            for j in range(n):
                image[index][j] = self.invert(image[index][j])

        return image
