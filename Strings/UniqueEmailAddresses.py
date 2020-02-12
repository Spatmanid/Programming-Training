# Date 11/02/2020
# @author Spyros Patmanidis
#
# References
# https://leetcode.com/problems/unique-email-addresses/
#
############### Unique Email Addresses ###############
# Every email consists of a local name and a domain name, separated by the @ sign.
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
# Besides lowercase letters, these emails may contain '.'s or '+'s.
# If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be forwarded # to the same address without dots in the local name.  For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to # the same email address.  (Note that this rule does not apply for domain names.)
# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain emails to  # be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain   # names.)
# It is possible to use both of these rules at the same time.
# Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 
# Note:
#   1 <= emails[i].length <= 100
#   1 <= emails.length <= 100
#   Each emails[i] contains exactly one '@' character.
#   All local and domain names are non-empty.
#   Local names do not start with a '+' character.
#
# Example 1:
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
#
# Solution
# 1. Seperate the email addresses into local and domain part
# 2. If local has the character '+' remove it along with everything beyond it
# 3. Remove all '.' from the local part
# 4. Canonical adrress = local + '@' + domain
#
# Complexity Analysis
# This solution has time complexity of O(C), where C is the total content of emails, and space complexity of O(C).

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            res = local.split('+')[0].replace('.', '') + '@' + domain
            unique.add(res)
        return len(unique)

def main():
    sol = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(sol.numUniqueEmails(emails))
    
if __name__ == "__main__":
    main()
