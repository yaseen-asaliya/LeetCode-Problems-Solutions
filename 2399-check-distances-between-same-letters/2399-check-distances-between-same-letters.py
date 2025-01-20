class Solution(object):
    def checkDistances(self, s, distance):
        first_occurrence = {}

        for i, char in enumerate(s):
            char_index = ord(char) - ord('a') 

            if char in first_occurrence:
                calculated_distance = i - first_occurrence[char] - 1
                if calculated_distance != distance[char_index]:
                    return False
            else:
                first_occurrence[char] = i

        return True