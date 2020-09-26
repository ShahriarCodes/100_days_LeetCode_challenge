class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        prev_profit = 0
        min = prices[0]
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
                
            profit = prices[i] - min
            if profit > prev_profit:
                prev_profit = profit
        
        return prev_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    instance = Solution()
    print(instance.maxProfit(prices))
