class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s = set()

        alphabetInMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.", "...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
            morseRep = ""
            for letter in word:
                morseRep += alphabetInMorse[ord(letter) -97]
            s.add(morseRep)
        
        return len(s)

