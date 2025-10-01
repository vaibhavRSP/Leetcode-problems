class Solution:
    def numWaterBottles(self, numBottles, numExchange):
        total_drunk = 0
        empty = 0
        full = numBottles

        while full > 0:
            total_drunk += full          
            empty += full                
            full = empty // numExchange 
            empty = empty % numExchange  

        return total_drunk
print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(15, 4))
