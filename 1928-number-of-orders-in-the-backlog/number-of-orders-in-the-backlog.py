class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buyBL = []
        sellBL = []

        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0:
                    if len(sellBL) == 0:
                        heapq.heappush(buyBL, (-price, amount))
                        break
                    sellPrice, sellAmount = heapq.heappop(sellBL)
                    if sellPrice <= price:
                        use = min(amount, sellAmount)
                        sellAmount -= use
                        amount -= use
                        if sellAmount > 0:
                            heapq.heappush(sellBL, (sellPrice, sellAmount))
                    else:
                        heapq.heappush(buyBL, (-price, amount))
                        heapq.heappush(sellBL, (sellPrice, sellAmount))
                        break
            else:
                while amount > 0:
                    if len(buyBL) == 0:
                        heapq.heappush(sellBL, (price, amount))
                        break
                    buyPrice, buyAmount = heapq.heappop(buyBL)
                    buyPrice = -buyPrice
                    if buyPrice >= price:
                        use = min(amount, buyAmount)
                        buyAmount -= use
                        amount -= use
                        if buyAmount > 0:
                            heapq.heappush(buyBL, (-buyPrice, buyAmount))
                    else:
                        heapq.heappush(sellBL, (price, amount))
                        heapq.heappush(buyBL, (-buyPrice, buyAmount))
                        break
        total = 0
        mod = 10**9 + 7
        for _, amount in buyBL:
            total += (amount % mod)
        for _, amount in sellBL:
            total += (amount % mod)
        return total % mod