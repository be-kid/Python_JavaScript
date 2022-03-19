const LIS = function (arr) {
  arr.unshift(Number.NEGATIVE_INFINITY);
  const dp = Array(arr.length).fill(-1);

  const find = (start) => {
    if (dp[start] !== -1) {
      return dp[start];
    }
    let result = 0;
    for (let nxt = start + 1; nxt < arr.length; nxt++) {
      if (arr[start] < arr[nxt]) {
        result = Math.max(result, find(nxt) + 1);
      }
    }
    dp[start] = result;
    return result;
  };

  return find(0);
};

let output = LIS([3, 2]);
console.log(output); // --> 1 (3 or 2)

output = LIS([3, 10, 2, 1, 20]);
console.log(output); // --> 3 (3, 10, 20)
