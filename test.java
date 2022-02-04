class test {
    public static void main(String[] args) {
        int[] gameState = {2, 2, 2, 2, 2, 2, 2, 2, 2};
        int[][] winPositions = {{0, 1, 2}, {3, 4, 5}, {6, 7, 8}};
        for (int[] winPosition: winPositions){
            System.out.println(gameState[winPosition[0]]);
            System.out.println(gameState[winPosition[1]]);
            System.out.println(gameState[winPosition[2]]);
        }
    }
}