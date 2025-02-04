class Solution:
    def invert(self, num):
        return 0 if num else 1

    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image) 

        for index in range(n):
            p1 = 0
            for p2 in range(n - 1, n // 2 - 1, -1):  
                image[index][p1], image[index][p2] = image[index][p2], image[index][p1]
                image[index][p1] = self.invert(image[index][p1])
                image[index][p2] = self.invert(image[index][p2])
                p1 += 1
            
            if n % 2 == 1:
                mid = n // 2
                image[index][mid] = self.invert(image[index][mid])

        return image
