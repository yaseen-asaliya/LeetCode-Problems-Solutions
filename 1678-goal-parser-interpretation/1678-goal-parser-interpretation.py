class Solution:
    def interpret(self, command: str) -> str:
        dic = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al'
        }
        res = ""
        tmp = ""

        for index in range(len(command)):
            tmp+=command[index]
            if(tmp in dic):
                res+=dic[tmp]
                tmp=""

        return res 

