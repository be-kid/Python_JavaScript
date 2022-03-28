const coinChange = function (total, coins) {
  const dp = Array.from({ length: coins.length + 1 }, (v) =>
    Array.from({ length: total + 1 }, (v) => Number.MAX_SAFE_INTEGER)
  );
  dp[0][0] = 1;
  for (let i = 1; i <= total; i++) {
    dp[0][i] = 0;
  }
  for (let i = 1; i <= coins.length; i++) {
    for (let j = 0; j <= total; j++) {
      if (j === 0) {
        dp[i][j] = 1;
      } else {
        if (j - coins[i - 1] >= 0) {
          dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]];
        } else {
          dp[i][j] = dp[i - 1][j];
        }
      }
    }
  }
  return dp[coins.length][total];
};

console.log(coinChange(4, [1, 2, 3]));
