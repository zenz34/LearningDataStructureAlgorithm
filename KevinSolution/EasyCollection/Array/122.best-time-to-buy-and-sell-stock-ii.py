from itertools import chain, islice

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfit2(prices)

    def maxProfit2(self, prices: List[int]) -> int:
        """
        Same as `maxProfit1()` but doesn't use itertools.
        """
        
        profit = 0

        for i in range(1, len(prices)):
            if prices[i - 1] < prices[i] :
                profit += prices[i] - prices[i - 1] 

        return profit

    def maxProfit1(self, prices: List[int]) -> int:
        """
        Leetcode optimal solution. Pretend you can buy-sell on the same day because
        the sum of profits of the small hills is equal to the profit of the full hill.
        
        Use itertools.
        """
        
        profit = 0

        for previous_price, current_price in zip(
            islice(prices, max(len(prices) - 1, 0)), # 0 in case length is 0.
            islice(prices, 1, None)
        ):
            if previous_price < current_price:
                profit += current_price - previous_price

        return profit
    
    def maxProfit0(self, prices: List[int]) -> int:
        """
        Use the greedy approach - buy low and sell high at the ends of increasing subsequences.
        Define increasing subsequence:
        ```
        allows previous_element <= current_element
        ```
        Note the less than or EQUAL to.
        
        The reasoning for this is because if you have an increasing subsequence, the max profit
        you can make from that subsequence is from buying and selling at the ends and not
        partitioning up the subsequence in multiple buy-sell pairs.
        
        Here is visual reasoning:
        Below is a subsequence somewhere in the middle of `prices`. The line represents a linearly
        increasing axis of price. So the increase in price `a - b` is less than `c - b`, since
        the line is shorter.

         current_low  a  b      c   current_high
        ...---|-------|--|------|--------|---...

        Because you can't buy and sell on the same day, partitioning up the subsequence into
        multiple buy-sells, will lower your profit.
        For example, if you buy-sell like so:
        ```
        a - current_low
        current_high - b # can't `- a` because sold `a` above so can't buy `a` on same day
        ```
        Then you are missing profit from `b - a`
        
        You are better off doing `current_high - current_low` and getting the full profit of the
        subsequence.
        
        The solution is to keep track of the current low and high of each increasing subsequence
        and buy on the low, sell on the high, and skip the intermediate increasing days.
        
        Earlier, I said I allow my increasing subsequences to be less than or EQUAL to.
        Here is an explanation why that is allowed.

        To represent that, you just have another day where stock is equal to previous day.
                      a
         current_low  b  c      d   current_high
        ...---|-------|--|------|--------|---...
        
        Now you can buy-sell like so:
        ```
        a - current_low
        current_high - b # allowed since `a` and `b` are actually different days
        ```
        But your profit is still the same as doing `current_high - current_low`.
        So it's a tiny bit more efficient in code to allow `<=` since there's less logic
        to increase the current subsequence length more often compared to selling more often.
        """

        current_low = 0
        current_high = 0
        
        profit = 0
        
        # Pad start with `float('inf')` to trigger a fake sell of `0 - 0` on the first day.
        # This triggers the `else` clause in for-loop below.
        previous_prices = chain(
            (float('inf'),),
            prices,
        )
        
        # Pad end with `-float('inf')` to trigger a sell at the very end.
        # This triggers the `else` clause in the for-loop below.
        # We need to do this because the way we track the end of an increasing subsequence
        # is by finding that the element decreases from the day before.
        # If we didn't do this, we would hold on to an increasing subsequence of length 1+
        # and not sell it.
        # An alternative is to sell in the `return`, but I like to keep the logic in the
        # for-loop, if possible.
        current_prices = chain(
            prices,
            (-float('inf'),)
        )
        
        for previous_price, current_price in zip(previous_prices, current_prices):
            if previous_price <= current_price: # add element to increasing subsequence
                current_high = current_price
            else: # sell and restart increasing subsequence
                profit += current_high - current_low
                current_low = current_high = current_price
                
        return profit
