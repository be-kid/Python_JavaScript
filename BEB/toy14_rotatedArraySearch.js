const rotatedArraySearch = function (rotated, target) {
  let start = 0;
  let end = rotated.length - 1;

  while (start <= end) {
    const mid = parseInt((start + end) / 2);
    if (rotated[mid] === target) {
      return mid;
    }

    if (rotated[mid] < target) {
      if (rotated[end] >= target) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    } else {
      if (rotated[start] <= target) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }
  }
  return -1;
};

let arr = [];
for (let i = 40; i < 100; i++) {
  arr.push(i);
}
for (let i = 0; i < 40; i++) {
  arr.push(i);
}
// [40, ... 100, 0, 1, ... 39]
let output = rotatedArraySearch(arr, 75);
console.log(output); // --> 35

output = rotatedArraySearch([4, 5, 6, 0, 1, 2, 3], 2);
console.log(output); // --> 5

output = rotatedArraySearch([4, 5, 6, 0, 1, 2, 3], 100);
console.log(output); // --> -1

output = rotatedArraySearch([3, 4, 5, 2], 4);
console.log(output); // --> 1
output = rotatedArraySearch([4, 5, 6, 0, 1, 2, 3], 1);
console.log(output); // --> 4
output = rotatedArraySearch([9, 10, 15, 4, 6, 8], 6);
console.log(output); // --> 4
output = rotatedArraySearch([10, 11, 12, 3, 6, 7, 8, 9], 11);
console.log(output); // --> 1
output = rotatedArraySearch([1, 2, 3], 5);
console.log(output); // --> -1
