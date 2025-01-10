class Solution(object):
    def numUniqueEmails(self, emails):
        
        for index in range(len(emails)):
            prefix, suffix = emails[index].split('@')
            prefix = prefix.replace('.', '')
            num_of_plus = prefix.count('+')

            if not num_of_plus:
                emails[index] = prefix + '@' + suffix
                continue
            emails[index] = prefix.split('+')[0] + '@' + suffix

        return len(set(emails))



        