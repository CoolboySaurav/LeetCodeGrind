class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        result = []
        Transaction = collections.namedtuple('Transaction', ['name', 'time', 'amount', 'city'])
        txnTuple = []
        
        for trans in transactions:
            _name, _time, _amount, _city = (int(val) if val.isdigit() else val for val in trans.split(","))
            txnTuple.append(Transaction(_name, _time, _amount, _city))
        
        n = len(transactions)
        validity = [True]*n
        
        for i in xrange(n):
            if txnTuple[i].amount > 1000:
                validity[i] = False
            for j in xrange(i+1, n):
                if (txnTuple[i].name == txnTuple[j].name) and (txnTuple[i].city != txnTuple[j].city) and abs(txnTuple[i].time - txnTuple[j].time) <= 60:
                    validity[i] = validity[j] = False
        
        for i in xrange(n):
            if not validity[i]:
                result.append(transactions[i])
        
        return result