class Vector2D {

    int row;
    int col;
    int[][] vector;
    int rowSize;

    public Vector2D(int[][] vec) {
        row = 0;
        col = 0;
        vector = vec;
        rowSize = vec.length;
    }
    
    public int next() {
        int result = -1;
        if (row < rowSize) {
            if (col < vector[row].length) {
                result = vector[row][col];
                col++;
            } else {
                row++;
                col = 0;
                return next();
            }
        }
        return result;
    }
    
    public boolean hasNext() {
        if (row < rowSize) {
            if (col < vector[row].length) {
                return true;
            } else {
                row++;
                col = 0;
                return hasNext();
            }
        }
        return false;
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D obj = new Vector2D(vec);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */