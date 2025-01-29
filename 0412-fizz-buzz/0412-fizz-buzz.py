class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []

        for index in range(n):
            if (index+1) % 3 == 0 and (index+1) % 5 == 0:
                answer.append("FizzBuzz")
            elif (index+1) % 3 == 0:
                answer.append("Fizz")
            elif (index+1) % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(index+1))
        
        return answer

