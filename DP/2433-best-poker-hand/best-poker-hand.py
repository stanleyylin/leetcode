class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rank_count = Counter(ranks)
        if len(set(suits)) <= 1:
            return "Flush"
        
        for _, freq in rank_count.most_common():
            if freq >= 3:
                return "Three of a Kind"
            elif freq == 2:
                return "Pair"
            else:
                return "High Card"
    
