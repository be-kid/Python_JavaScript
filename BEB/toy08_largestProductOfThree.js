const largestProductOfThree = function (arr) {
  // 음수가 없으면 최대값 3개
  // 음수가 1개면 최대값 3개
  // 음수가 2개 이상이면 최소값 2개와 최대값 혹은 그냥 최대값 3개
  // 음수만 있으면 최대값 3개
  arr.sort((a, b) => a - b);

  // 최대값 3개 vs 최소값 2개 + 최대값 1개 해서 더 큰거 하면 되네
  const case1 = arr[0] * arr[1] * arr[arr.length - 1];
  const case2 = arr.pop() * arr.pop() * arr.pop();
  return case1 > case2 ? case1 : case2;
};
