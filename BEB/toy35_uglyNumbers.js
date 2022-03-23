const uglyNumbers = function (n) {
  const uglyNumbers = [1];
  let idx2 = 0,
    idx3 = 0,
    idx5 = 0;

  for (let i = 0; i < n; i++) {
    const next2 = uglyNumbers[idx2] * 2;
    const next3 = uglyNumbers[idx3] * 3;
    const next5 = uglyNumbers[idx5] * 5;

    const nextUglyNum = Math.min(next2, next3, next5);
    uglyNumbers.push(nextUglyNum);

    if (nextUglyNum === next2) idx2++;
    if (nextUglyNum === next3) idx3++;
    if (nextUglyNum === next5) idx5++;
  }
  return uglyNumbers[n - 1];
};

let result = uglyNumbers(1000);
console.log(result);
