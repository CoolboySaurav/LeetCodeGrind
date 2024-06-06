class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_set = set(s)
        maxlen = 0

        for c in char_set:
            l = 0
            count = 0

            for r in range(len(s)):
                if s[r] != c:
                    count += 1

                while count > k:
                    if s[l] != c:
                        count -= 1
                    l += 1

                maxlen = max(maxlen, r - l + 1)

        return maxlen