import java.util.*;
class Solution {
    private static char[][] board;
    private static int answer;
    
    public int solution(int n) {
        board = new char[n][n];
        for (char[] row : board) {
            Arrays.fill(row, '.');
        }
        backtracking(0, n);
        
        return answer;
    }
    
    private void backtracking(int row, int n) {
        if (row == n) {
            answer++;
            return;
        }
        
        for (int col = 0; col < n; col++) {
            if (isValid(row, col, n)) {
                board[row][col] = 'Q';
                backtracking(row + 1, n);
                board[row][col] = '.';
            }
        }
    }
    
    private boolean isValid(int row, int col, int n) {
        // 세로 방향 체크
        for (int r = 0; r < row; r++) {
            if (board[r][col] == 'Q') return false;
        }
        
        // 왼쪽 상단 대각선 체크
        int r = row - 1;
        int c = col - 1;
        while (r >= 0 && c >= 0) {
            if (board[r][c] == 'Q') return false;
            r--;
            c--;
        }
        
        // 오른쪽 상단 대각선 체크
        r = row - 1;
        c = col + 1;
        while (r >= 0 && c < n) {
            if (board[r][c] == 'Q') return false;
            r--;
            c++;
        }
        
        return true;
    }
}