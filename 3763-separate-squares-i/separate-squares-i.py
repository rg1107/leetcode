class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        left = min([square[1] for square in squares])
        right = max([square[1] + square[2] for square in squares])

        print(left, right)

        def calcArea(squares, y):
            a_down = 0
            a_up = 0
            for sq in squares:
                x,y_i,l = sq

                if y >= y_i + l:
                    a_down += l*l
                elif y_i >= y:
                    a_up += l*l
                else:
                    a_down += l*(y - y_i)
                    a_up += l*(y_i + l - y)
            
            return a_up - a_down
        
        while (right - left) > pow(10, -6):
            
            mid = (right + left) / 2
            diff = calcArea(squares, mid)
            if diff > 0:
                left = mid
            else:
                right = mid
        
        return right




        