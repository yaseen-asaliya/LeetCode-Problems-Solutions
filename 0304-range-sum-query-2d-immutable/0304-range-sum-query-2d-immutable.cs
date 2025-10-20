public class NumMatrix
{
    private int[][] prefix; 

    public NumMatrix(int[][] matrix)
    {
        int rows = matrix.Length;
        if (rows == 0) return;
        int cols = matrix[0].Length;

        prefix = new int[rows][];
        for (int i = 0; i < rows; i++)
        {
            prefix[i] = new int[cols + 1]; 

            for (int j = 0; j < cols; j++)
            {
                prefix[i][j + 1] = prefix[i][j] + matrix[i][j];
            }
        }
    }

    public int SumRegion(int row1, int col1, int row2, int col2)
    {
        int res = 0;
        for (int i = row1; i <= row2; i++)
        {
            res += prefix[i][col2 + 1] - prefix[i][col1];
        }
        return res;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.SumRegion(row1,col1,row2,col2);
 */