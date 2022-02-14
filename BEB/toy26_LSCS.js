const LSCS = function (arr) {
  let result = arr[0];

  let sum = [arr[0]];
  for (let i = 1; i < arr.length; i++) {
    if (sum[i - 1] < 0) {
      sum.push(arr[i]);
    } else {
      sum.push(sum[i - 1] + arr[i]);
    }
    result = result < sum[i] ? sum[i] : result;
  }
  return result;
};
