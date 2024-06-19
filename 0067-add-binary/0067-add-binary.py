class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=""
        carry=0
        a=a[::-1]
        b=b[::-1]
        for i in range(max(len(a),len(b))):
            A=ord(a[i])-ord("0") if i<len(a) else 0
            B=ord(b[i])-ord("0") if i<len(b) else 0
            total=(A+B+carry)
            carry=total//2
            res=str(total%2)+res
        if carry:
            res="1"+res
        return res