class Solution:
    def pourWater(self, heights: list[int], volume: int, k: int) -> list[int]:
        N = len(heights)
        j = k
        for drop in range(volume):
            
            while j > 0 and heights[j] >= heights[j-1]:
                j -= 1
            
            while j < N - 1 and heights[j] >= heights[j+1]:
                j += 1
            
            # If min valley is wide, water should be stored in leftmost empty space
            while j > k and heights[j] == heights[j-1]:
                j -= 1 
            
            heights[j] += 1
        return heights

        