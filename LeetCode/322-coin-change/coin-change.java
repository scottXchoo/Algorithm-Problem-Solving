class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int coinChange(int[] coins, int amount) {
        return dp(coins, amount);
    }

    private int dp(int[] coins, int amount) {
        if (amount == 0) return 0;
        if (memo.containsKey(amount)) return memo.get(amount);

        int minCount = Integer.MAX_VALUE;
        for (int coin : coins) {
            int remainAmount = amount - coin;
            if (remainAmount >= 0) {
                int result = dp(coins, remainAmount);
                if (result != -1) {
                    minCount = Math.min(minCount, result + 1);
                }
            }
        }

        int result = (minCount == Integer.MAX_VALUE) ? -1 : minCount;
        memo.put(amount, result);
        return result;
    }
}