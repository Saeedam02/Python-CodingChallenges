# Container With Most Water
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

class Solution:
    def __init__(self, L1: list[int]) -> int:
        """
        Find two lines that together with the x-axis form a container, such that the container contains the most water.


        :param L1: List of Input.

        :returns: The max value of continer.
        """
        self.hieght = L1

    def MaxArea(self):
        new = list()
        if len(self.hieght) <= 1 :
            return " Invalied Input"
        
        for i in self.hieght :
            for j in self.hieght[i+1:]:
                new.append(i*j)

        Max_value = max(new)

        return Max_value
c = Solution([1,8,6,2,5,4,8,3,7])
print(c.MaxArea())