const knapsack = function (weight, items) {
  // items.length * (weight+1) 크기의 배열 필요
  const dp = Array.from({ length: items.length }, (v) => {
    return Array.from({ length: weight + 1 }, (v) => 0);
  });

  for (let i = 0; i < items.length; i++) {
    for (let j = 0; j < weight + 1; j++) {
      if (i === 0) {
        dp[i][j] = items[i][0] > j ? 0 : items[i][1];
      } else {
        if (items[i][0] > j) {
          dp[i][j] = dp[i - 1][j];
        } else {
          dp[i][j] = Math.max(
            dp[i - 1][j - items[i][0]] + items[i][1],
            dp[i - 1][j]
          );
        }
      }
    }
  }
  return dp[items.length - 1][weight];
};

let weight = 50;
let items = [
  [10, 60],
  [20, 100],
  [30, 120],
];
let output = knapsack(weight, items);
console.log(output); // --> 220 (items[1], items[2])

weight = 10;
items = [
  [5, 10],
  [4, 40],
  [6, 30],
  [3, 50],
];
output = knapsack(weight, items);
console.log(output); // --> 90 (items[1], items[3])

weight = 40;
items = [
  [40, 10],
  [50, 100],
  [10, 30],
];

output = knapsack(weight, items);
console.log(output); // --> 30 (items[2])
