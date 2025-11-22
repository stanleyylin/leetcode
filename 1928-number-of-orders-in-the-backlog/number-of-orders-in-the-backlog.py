class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyBL = []
        sellBL = []

        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0:
                    if not sellBL or sellBL[0][0] > price:
                        heapq.heappush(buyBL, (-price, amount))
                        break
                    sellPrice, sellAmount = heapq.heappop(sellBL)
                    use = min(amount, sellAmount)
                    sellAmount -= use
                    amount -= use
                    if sellAmount > 0:
                        heapq.heappush(sellBL, (sellPrice, sellAmount))
            else:
                while amount > 0:
                    if not buyBL or -buyBL[0][0] < price:
                        heapq.heappush(sellBL, (price, amount))
                        break
                    buyPrice, buyAmount = heapq.heappop(buyBL)
                    buyPrice = -buyPrice
                    use = min(amount, buyAmount)
                    buyAmount -= use
                    amount -= use
                    if buyAmount > 0:
                        heapq.heappush(buyBL, (-buyPrice, buyAmount))
        mod = 10**9 + 7
        total = (sum(b for _, b in buyBL)%mod) + (sum(s for _, s in sellBL)%mod)
        return total % mod