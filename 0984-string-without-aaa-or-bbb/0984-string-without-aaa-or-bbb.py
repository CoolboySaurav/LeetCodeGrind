class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        result = ""
        numA = a
        numB = b
        ca = "a"
        cb = "b"
        
        if numA < numB:
            numA, numB = numB, numA
            ca, cb = cb, ca
        
        
        while numA > 0:
            if numA > numB:
                result += ca
                numA -= 1
            if numA > 0:
                result += ca
                numA -= 1
            if numB > 0:
                result += cb
                numB -= 1
        
        return result