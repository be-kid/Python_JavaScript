// 좌표평면 위의 두 점 사이의 거리를 계산하는 함수입니다.
function calculateDistance(p1, p2) {
  const yDiff = p2[0] - p1[0];
  const xDiff = p2[1] - p1[1];
  return Math.round(Math.sqrt(Math.pow(yDiff, 2) + Math.pow(xDiff, 2)) * 100);
}

const merge = function (left, right, comparator = (item) => item) {
  let merged = [];
  let leftIdx = 0,
    rightIdx = 0;
  const size = left.length + right.length;

  for (let i = 0; i < size; i++) {
    if (leftIdx >= left.length) {
      merged.push(right[rightIdx]);
      rightIdx++;
    } else if (
      rightIdx >= right.length ||
      comparator(left[leftIdx]) <= comparator(right[rightIdx])
    ) {
      merged.push(left[leftIdx]);
      leftIdx++;
    } else {
      merged.push(right[rightIdx]);
      rightIdx++;
    }
  }
  return merged;
};

const mergeSort = function (arr, comparator) {
  const aux = (start, end) => {
    if (start >= end) return [arr[start]];
    const mid = Math.floor((start + end) / 2);
    const left = aux(start, mid);
    const right = aux(mid + 1, end);
    return merge(left, right, comparator);
  };
  return aux(0, arr.length - 1);
};

const closestPairOfPoints = function (points) {
  const bruteForce = (start, end, sorted) => {
    let min = Number.MAX_SAFE_INTEGER;
    for (let src = start; src <= end; src++) {
      for (let dst = src + 1; dst <= end; dst++) {
        const dist = calculateDistance(sorted[src], sorted[dst]);
        min = Math.min(min, dist);
      }
    }
    return min;
  };

  const closetCrossing = (mid, sorted, min) => {
    const strip = [];
    const midX = sorted[mid][1];
    let lIdx = mid - 1;
    let rIdx = mid + 1;

    while (
      rIdx < sorted.length &&
      Math.abs(midX - sorted[rIdx][1]) * 100 < min
    ) {
      rIdx++;
    }
    while (lIdx >= 0 && Math.abs(midX - sorted[lIdx][1]) * 100 < min) {
      lIdx--;
    }

    for (let i = lIdx + 1; i < rIdx; i++) {
      for (let j = i + 1; j < rIdx; j++) {
        min = Math.min(min, calculateDistance(sorted[i], sorted[j]));
      }
    }
    return min;
  };

  const closetFrom = (start, end, size, sorted) => {
    if (size <= 3) {
      return bruteForce(start, end, sorted);
    }
    const mid = Math.floor((start + end) / 2);
    const minLeft = closetFrom(start, mid, mid - start + 1, sorted);
    const minRight = closetFrom(mid + 1, end, end - mid, sorted);

    let min = Math.min(minLeft, minRight);
    return closetCrossing(mid, sorted, min);
  };

  const sorted = mergeSort(points.slice(0), (item) => item[1]);
  return closetFrom(0, sorted.length - 1, sorted.length, sorted);
};

let points = [
  [0, 0],
  [1, 3],
  [2, 2],
];
let output = closestPairOfPoints(points);
console.log(output); // --> 141 ([1, 3], [2, 2])
/*
  3 |  x
  2 |     x
  1 |       
  0 | x 
  ------------
      0 1 2 3 
  */

points = [
  [0, 0],
  [0, 1],
  [0, 3],
  [0, 5],
];
output = closestPairOfPoints(points);
console.log(output); // --> 100 ([0, 0], [0, 1])
/*
  5 | x
  4 | 
  3 | x
  2 |     
  1 | x     
  0 | x 
  ------------
      0 1 2 3 
  */
