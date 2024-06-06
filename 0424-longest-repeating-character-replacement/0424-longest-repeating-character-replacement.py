class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = defaultdict(int)
        l = 0
        maxlen = maxfreq = 0
        
        for r in range(len(s)):
            char_count[s[r]] += 1
            maxfreq = max(maxfreq, char_count[s[r]])
            
            # Check if the current window size minus the frequency of the most common character is greater than k
            if (r - l + 1) - maxfreq > k:
                char_count[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, (r - l + 1))
        
        return maxlen
        
#         char_set = set(s)
#         maxlen = 0

#         for c in char_set:
#             l = 0
#             count = 0

#             for r in xrange(len(s)):
#                 if s[r] != c:
#                     count += 1

#                 while count > k:
#                     if s[l] != c:
#                         count -= 1
#                     l += 1

#                 maxlen = max(maxlen, r - l + 1)

#         return maxlen