function power(base, exponent) {
  const mod = 94906249;
  let memo = { 0: 1 };
  if (exponent === 0) {
    return 1;
  }

  function solution(base, exponent) {
    if (exponent === 1) {
      memo[exponent] = base;
      return base;
    } else {
      if (memo[exponent]) {
        return memo[exponent];
      } else {
        if (exponent % 2 === 0) {
          const temp =
            (solution(base, exponent / 2) * solution(base, exponent / 2)) % mod;
          memo[exponent] = temp;

          return memo[exponent];
        } else {
          const temp =
            (((solution(base, (exponent - 1) / 2) *
              solution(base, (exponent - 1) / 2)) %
              mod) *
              (base % mod)) %
            mod;
          memo[exponent] = temp;

          return memo[exponent];
        }
      }
    }
  }
  // console.log(memo);
  return solution(base % mod, exponent % mod);
}
console.log(power(3, 5));
