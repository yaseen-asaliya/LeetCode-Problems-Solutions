class Solution:
    def countPoints(self, rings: str) -> int:
        my_dict = {}
        c = 0

        for i in range(1, len(rings), 2):
            my_dict[rings[int(i)]] = my_dict.get(rings[int(i)], set())

            my_dict[rings[int(i)]].add(rings[i-1])

        for _, value in my_dict.items():
            if (len(value)) == 3:
                c+=1

        return c
