const LCS = function (str1, str2) {
  const dp = Array.from({ length: str1.length + 1 }, () =>
    Array.from({ length: str2.length + 1 }, () => 0)
  );

  for (let i = 0; i < str1.length; i++) {
    for (let j = 0; j < str2.length; j++) {
      if (str1[i] === str2[j]) {
        dp[i + 1][j + 1] = dp[i][j] + 1;
      } else {
        dp[i + 1][j + 1] =
          dp[i + 1][j] < dp[i][j + 1] ? dp[i][j + 1] : dp[i + 1][j];
      }
    }
  }
  return dp[str1.length][str2.length];
};

let output = LCS("abcd", "aceb");
console.log(output); // --> 2 ('ab' or 'ac')

output = LCS("acaykp", "capcak");
console.log(output); // --> 4 ('acak')

output = LCS("1c2o3d4d5e", "ss1tt2aa3tt4ee5ss");
console.log(output); // 5
