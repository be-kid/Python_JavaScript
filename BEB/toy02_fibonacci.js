function fibonacci(n) {
  const dp = [0, 1];

  function solution(x) {
    if (x === n) {
      return dp[x];
    }
    dp.push(dp[x] + dp[x + 1]);
    return solution(x + 1);
  }

  return solution(0);
}
