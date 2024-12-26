class Solution(object):
   def sortPeople(self, names, heights):
        people = list(zip(heights, names))

        people.sort(reverse=True, key=lambda x: x[0])

        return [name for _, name in people]

