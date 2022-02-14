function divideChocolateStick(M, N) {
  // 6 12

  // 1 6 12
  // 2 3 6
  // 3 2 4
  // 6 1 2

  // 최대공약수를 구하고
  // 최대공약수의 약수로
  let gcdNum = M > N ? gcd(M, N) : gcd(N, M);
  let nums = {};
  let i = 0;
  while (i <= Math.sqrt(gcdNum)) {
    if (gcdNum % i === 0) {
      nums[i] = 1;
      nums[gcdNum / i] = 1;
    }
    i += 1;
  }

  return Object.keys(nums).map((elem) => [parseInt(elem), M / elem, N / elem]);
}

function gcd(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

console.log(divideChocolateStick(4, 8));
