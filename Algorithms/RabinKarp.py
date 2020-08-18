# Date 18/08/2020
# @author Spyros Patmanidis
#
#
# Rabin Karp Algorithm
#
# Several string-matching algorithms, including the Knuth–Morris–Pratt algorithm
# and the Boyer–Moore string-search algorithm, reduce the worst-case time for string
# matching by extracting more information from each mismatch, allowing them to skip
# over positions of the text that are guaranteed not to match the pattern. 
# The Rabin–Karp algorithm instead achieves its speedup by using a hash function 
# to quickly perform an approximate check for each position, and then only performing
# an exact comparison at the positions that pass this approximate check.
# 
# A hash function is a function which converts every string into a numeric value,
# called its hash value; for example, we might have hash("hello")=5. If two strings are
# equal, their hash values are also equal. For a well-designed hash function, the opposite
# is true, in an approximate sense: strings that are unequal are very unlikely to have equal
# hash values. The Rabin–Karp algorithm proceeds by computing, at each position of the text,
# the hash value of a string starting at that position with the same length as the pattern.
# If this hash value equals the hash value of the pattern, it performs a full comparison at 
# that position.
# 
# In order for this to work well, the hash function should be selected randomly from a family
# of hash functions that are unlikely to produce many false positives, positions of the text 
# which have the same hash value as the pattern but do not actually match the pattern. These
# positions contribute to the running time of the algorithm unnecessarily, without producing 
# a match. Additionally, the hash function used should be a rolling hash, a hash function 
# whose value can be quickly updated from each position of the text to the next. Recomputing 
# the hash function from scratch at each position would be too slow. 
#
# Time Complexity
# The average and best case running time of the Rabin-Karp algorithm is O(𝑛+𝑚), but its worst-case
# time is O(𝑛⋅𝑚). Worst case of Rabin-Karp algorithm occurs when all characters of pattern and text
# are same as the hash values of all the substrings of 𝑡𝑥𝑡[] match with hash value of 𝑝𝑎𝑡[].
# For example 𝑝𝑎𝑡[] = “𝐴𝐴𝐴” and 𝑡𝑥𝑡[] = “𝐴𝐴𝐴𝐴𝐴𝐴𝐴”.

class Solution:
    def rabin_karp(self, pattern, text):
        m, n = len(pattern), len(text)
        if m > n: return -1
        
        pattern = pattern.lower()
        text = text.lower()
        
        prime = 37
        p_hash = 0
        t_hash = 0
        for i in range(m):
            p_hash += (ord(pattern[i]) - ord('a') + 1) * (prime ** i)
            t_hash += (ord(text[i]) - ord('a') + 1) * (prime ** i)
        
        if p_hash == t_hash and text[:m] == pattern:
            return 0
        for i in range(m, n):
            t_hash -= (ord(text[i-m]) - ord('a') + 1)
            t_hash //= prime
            t_hash += (ord(text[i]) - ord('a') + 1) * (prime ** (m-1))
            if t_hash == p_hash and text[i-m+1:i+1] == pattern:
                return i-m+1
        return -1
    
    def rabin_karp_count(self, pattern, text):
        m, n = len(pattern), len(text)
        if m > n: return 0
        
        pattern = pattern.lower()
        text = text.lower()
        
        prime = 3
        p_hash = 0
        t_hash = 0
        for i in range(m):
            p_hash += (ord(pattern[i]) - ord('a') + 1) * (prime ** i)
            t_hash += (ord(text[i]) - ord('a') + 1) * (prime ** i)
        
        counter = 0
        
        if p_hash == t_hash and text[:m] == pattern:
            counter += 1

        for i in range(m, n):
            t_hash -= (ord(text[i-m]) - ord('a') + 1)
            t_hash //= prime
            t_hash += (ord(text[i]) - ord('a') + 1) * (prime ** (m-1))
            if t_hash == p_hash and text[i-m+1:i+1] == pattern:
                counter += 1
        
        return counter
