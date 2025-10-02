class Solution:
    def maxBottlesDrunk(self, numBottles, numExchange):
        total_drunk = 0
        empty = 0
        while numBottles > 0:
            total_drunk += numBottles
            empty += numBottles
            numBottles = 0
            if empty >= numExchange:
                numBottles = 1
                empty -= numExchange
                numExchange += 1
            else:
                break
        
        return total_drunk
