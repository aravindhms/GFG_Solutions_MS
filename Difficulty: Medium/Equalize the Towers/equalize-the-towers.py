class Solution:
    def minCost(self, heights, cost):
        # code here
        combined = sorted(zip(heights, cost))
        total_cost_weight = sum(cost)
        
        cumulative_weight = 0
        median_height = 0
        for h, c in combined:
            cumulative_weight += c
            if cumulative_weight >= (total_cost_weight + 1) / 2:
                median_height = h
                break
        
        min_total_cost = 0
        for h, c in combined:
            min_total_cost += abs(h - median_height) * c
            
        return min_total_cost
        