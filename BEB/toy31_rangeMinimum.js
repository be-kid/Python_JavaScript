const rangeMinimum = function (arr, ranges) {
  const findMultiple = (n) => {
    let temp = 1;
    let count = 0;
    while (true) {
      if (n <= temp) {
        return temp;
      }
      temp = temp * 2;
      count += 1;
    }
  };
  const segSize = findMultiple(arr.length);
  const segTree = Array(segSize * 2).fill(0);

  const makeSegTree = (start, end, idx) => {
    if (start === end) {
      segTree[idx] = arr[start];
      return segTree[idx];
    }
    const mid = parseInt((start + end) / 2);
    const left = makeSegTree(start, mid, idx * 2);
    const right = makeSegTree(mid + 1, end, idx * 2 + 1);
    segTree[idx] = left < right ? left : right;
    return segTree[idx];
  };

  makeSegTree(0, arr.length - 1, 1);
  //console.log(segTree);
  const findMinNum = (start, end, left, right, now) => {
    //console.log(start, end, left, right, now);
    if (start > right || end < left) {
      return Infinity;
    }
    if (start >= left && right >= end) {
      //console.log(start, end, left, right, now);
      return segTree[now];
    }

    const mid = parseInt((start + end) / 2);

    let leftPart = findMinNum(start, mid, left, right, now * 2);
    let rightPart = findMinNum(mid + 1, end, left, right, now * 2 + 1);

    //console.log(start, mid, end, left, right, now, ":", leftPart, rightPart);
    return leftPart < rightPart ? leftPart : rightPart;
  };
  const result = [];
  for (let range of ranges) {
    result.push(findMinNum(0, arr.length - 1, range[0], range[1], 1));
  }
  return result;
};

const arr = [1, 3, 2, 7, 9, 11];
const mins = rangeMinimum(arr, [
  [1, 4],
  [0, 3],
]);
console.log(mins); // --> [2, 1]

console.log(rangeMinimum([1, 2, 3], [[1, 1]]));
console.log(
  rangeMinimum(
    [10, 11, 12, 3, 6, 7, 8, 9],
    [
      [4, 7],
      [0, 2],
    ]
  )
);
