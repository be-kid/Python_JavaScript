function orderOfPresentation(N, K) {
  const factorial = [1];
  const check = Array(N + 1).fill(0);
  for (let i = 1; i < 12; i++) {
    factorial.push(factorial[i - 1] * i);
  }
  let result = 0;
  for (let i = 0; i < N; i++) {
    result += (K[i] - 1 - checkUsed(check, K[i])) * factorial[N - i - 1];
    check[K[i]] = 1;
  }

  return result;

  // 이미 앞에서 정해진 숫자들 중에서 자기보다 작은게 있으면 그거는 제외해야한다

  // 7 3 4 2 5 1 6 / 7

  // 6 * 6! -> 7 확정
  // 2 * 5! -> 7,3 확정
  // 2 * 4! -> 7,3,4 확정
  // 1 * 3! -> 7,3,4,2 확정
  // 1 * 2! -> 7,3,4,2,5 확정
  // 0 * 1! -> 7,3,4,2,5,1 확정
  // 0 * 0! -> 7,3,4,2,5,1,6
}
function checkUsed(check, num) {
  let count = 0;
  for (let i = 1; i < num; i++) {
    if (check[i] === 1) {
      count += 1;
    }
  }
  return count;
}
