class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        counter = 0
        my_list = []
        for i in nums:
            counter = i + counter
            my_list.append(counter)

        return (my_list)

