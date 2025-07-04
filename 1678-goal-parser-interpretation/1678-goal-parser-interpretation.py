class Solution:
    def interpret(self, command: str) -> str:
        dic = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }
        res = ""

        for index in range(len(command)):
            if command[index] == 'G':
                res += dic['G']
            elif command[index] == '(' and command[index+1] == ')':
                res += dic['()']
                index += 2
            elif command[index] == '(' and command[index+1] == 'a':
                res += dic['(al)']
                index += 5
        
        return res 

