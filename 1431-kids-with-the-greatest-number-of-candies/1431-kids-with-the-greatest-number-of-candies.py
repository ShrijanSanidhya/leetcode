class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)

        ans = []

        for candy in candies:
            ans.append(candy + extraCandies >= max_candies)

        return ans