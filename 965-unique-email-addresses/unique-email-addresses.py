class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            email_sep = email.split("@")
            domain = email_sep[0]
            address = email_sep[1]
            if '+' in domain:
                domain = domain[:domain.index('+')]
            domain = domain.replace('.','')
            s.add(domain+'@'+address)
        return len(s)

                
