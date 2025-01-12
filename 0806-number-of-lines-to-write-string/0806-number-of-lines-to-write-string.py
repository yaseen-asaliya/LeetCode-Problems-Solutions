class Solution(object):
    def numberOfLines(self, widths, s):
        cummulative_count = 0
        num_of_lines = 1 

        for index in range(len(s)):
            char_width = widths[ord(s[index]) - ord('a')]
            if cummulative_count + char_width > 100:
                num_of_lines += 1 
                cummulative_count = char_width 
            else:
                cummulative_count += char_width

        return [num_of_lines, cummulative_count]
    

