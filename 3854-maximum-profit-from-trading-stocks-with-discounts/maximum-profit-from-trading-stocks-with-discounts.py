class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        employee_tree = defaultdict(list)
        for u, v in hierarchy:
            employee_tree[u].append(v)
            
        def merge(A, B):
            INF = float('-inf')
            C = [INF] * (budget + 1)
            for cost_a in range(budget + 1):
                val_a = A[cost_a]
                if val_a <= INF/2:  # Early skip of invalid states
                    continue
                for cost_b in range(budget + 1 - cost_a):
                    val_b = B[cost_b]
                    if val_b <= INF/2:
                        continue
                    C[cost_a + cost_b] = max(C[cost_a + cost_b], val_a + val_b)
            return C
            
        def dfs(emp):
            INF = float('-inf')
            # Initialize arrays for both scenarios
            # When parent didn't buy
            skip_no_parent = [0] + [INF] * budget  # not buying
            buy_no_parent = [INF] * (budget + 1)   # buying at full price
            
            # When parent bought
            skip_parent = [0] + [INF] * budget     # not buying
            buy_parent = [INF] * (budget + 1)      # buying at half price
            
            # Calculate costs and profits
            full_cost = present[emp - 1]
            half_cost = full_cost // 2
            profit_full_cost = future[emp - 1] - full_cost
            profit_half_cost = future[emp - 1] - half_cost
            
            # Set initial profits for buying cases
            if full_cost <= budget:
                buy_no_parent[full_cost] = profit_full_cost
            if half_cost <= budget:
                buy_parent[half_cost] = profit_half_cost
                
            # Process children
            for child in employee_tree[emp]:
                dp_no_parent, dp_parent = dfs(child)
                
                # Merge each scenario with child results
                skip_no_parent = merge(skip_no_parent, dp_no_parent)
                buy_no_parent = merge(buy_no_parent, dp_parent)
                skip_parent = merge(skip_parent, dp_no_parent)
                buy_parent = merge(buy_parent, dp_parent)
            
            # Combine results for each parent state
            dp_no_parent = [max(skip_no_parent[i], buy_no_parent[i]) 
                          for i in range(budget + 1)]
            dp_parent = [max(skip_parent[i], buy_parent[i]) 
                        for i in range(budget + 1)]
            
            return dp_no_parent, dp_parent
        
        result_no_parent, _ = dfs(1)
        return max(0, max(result_no_parent))