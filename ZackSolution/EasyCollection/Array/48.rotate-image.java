class RotateImage {
    public void rotate_4corner_recursion(int[][] matrix, int topX, int leftY, int bottomX, int rightY) {
        // even number, 1 element left, equal , odd number, less
        if (topX >= bottomX || leftY >= rightY) {
            return;
        }

        int times = bottomX - topX;

        for (int i = 0; i < times; i++) {
            int topLeftElement = matrix[topX][leftY + i];
            int topRightElement = matrix[topX + i][rightY];
            int bottomRightElement = matrix[bottomX][rightY - i];
            int bottomLeftElement = matrix[bottomX - i][leftY];

            matrix[topX + i][rightY] = topLeftElement;

            matrix[bottomX][rightY - i] = topRightElement;

            matrix[bottomX - i][leftY] = bottomRightElement;

            matrix[topX][leftY + i] = bottomLeftElement;
        }

        rotate_4corner_recursion(matrix, 1 + topX, 1 + leftY, bottomX - 1, rightY - 1);
    }

    public void rotate_transpose_and_reverse(int[][] matrix) {
        int n = matrix.length;

        // transpose matrix
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                int tmp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = tmp;
            }
        }

        // reverse each row
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[i][n - j - 1];
                matrix[i][n - j - 1] = tmp;
            }
        }
    }

    public void rotate(int[][] matrix) {
        rotate_4corner_recursion(matrix, 0, 0, matrix.length - 1, matrix[0].length - 1);

        // rotate_transpose_and_reverse(matrix);
    }
}