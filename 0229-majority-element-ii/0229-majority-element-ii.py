class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Boyer-Moor Majority Voting Algorithm
        """
            Since we need to find element/s with majority > n/3
            there can be at max exactly two elements like that.
            (n/3 + 1)*3 > len(nums) 
        """
        # Counters for the potential majority elements
        count1 = count2 = 0     
        # Potential majority element candidates
        candidate1 = candidate2 = 0

        # First pass to find potential majority elements.
        for num in nums:
            # If count1 is 0 and the current number is not equal to candidate2, update candidate1.
            if count1 == 0 and num != candidate2:
                count1 = 1
                candidate1 = num

            # If count2 is 0 and the current number is not equal to candidate1, update candidate2.
            elif count2 == 0 and num != candidate1:
                count2 = 1
                candidate2 = num
            
            # Update counts for candidate1 and candidate2.
            elif candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

            # If the current number is different from both candidates, decrement their counts.
            else:
                count1 -= 1
                count2 -= 1

        result = []
        threshold = len(nums) // 3  # Threshold for majority element

        # Second pass to count occurrences of the potential majority elements.
        count1 = count2 = 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1

        # Check if the counts of potential majority elements are greater than n/3 and add them         to the result.
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)

        return result
        
        
        def countNum(num):
            count = 0
            for i in nums:
                if num == i:
                    count += 1
            return count
        
        
        
        n = len(nums)
        res = []
        countMap = defaultdict(int)
        
        for i in nums:
            countMap[i] += 1
            if len(countMap)>2:
                newCount = defaultdict(int)
                for i, v in countMap.items():
                    if v > 1:
                        newCount[i] = v - 1
                countMap = newCount
        
        for i in countMap.keys():
            if countNum(i) > n/3:
                res.append(i)
        
        return res