class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)

        dic = {}
        res = []
        for x, y, z in zip_longest(nums1, nums2, nums3, fillvalue=None):
            if not x == None and x not in dic:
                dic[x] = 1
            elif not x == None:
                dic[x] += 1

            if not y == None and y not in dic:
                dic[y] = 1
            elif not y == None:
                dic[y] += 1

            if not z == None and z not in dic:
                dic[z] = 1
            elif not z == None:
                dic[z] += 1
        
        for k, v in dic.items():
            if v >= 2:
                res.append(k)

        return res


        