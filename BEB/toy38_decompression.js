const decompression = function (image) {
  const solution = (x, y, n) => {
    if (n === 1) {
      return String(image[x][y]);
    }
    n = parseInt(n / 2);
    const a = solution(x, y, n);
    const b = solution(x, y + n, n);
    const c = solution(x + n, y, n);
    const d = solution(x + n, y + n, n);
    if (a + b + c + d === "0000" || a + b + c + d === "1111") {
      return a;
    } else {
      return "X" + a + b + c + d;
    }
  };

  return solution(0, 0, image.length);
};

let image = [
  [1, 0, 1, 1],
  [0, 1, 1, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 0],
];
let result = decompression(image);
console.log(result); // --> 'XX100110X1100​'

image = [
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [1, 1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 0, 1, 1],
  [1, 1, 1, 1, 0, 1, 1, 1],
];
result = decompression(image);
console.log(result); // --> 'X0X101X10101X00X10011'
