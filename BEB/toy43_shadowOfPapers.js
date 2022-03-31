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
    const right = aux(start, mid);
    const left = aux(mid + 1, end);
    return merge(left, right, comparator);
  };
  return aux(0, arr.length - 1);
};

function shadowOfPapers(papers) {
  const coordinates = [];
  papers.forEach((p) => {
    const [x, y, width, height] = p;
    coordinates.push([x, y, y + height - 1, 1]);
    coordinates.push([x + width, y, y + height - 1, -1]);
  });

  const sorted = mergeSort(coordinates, (c) => c[0]);
  const height = Array(10000 + 1).fill(0);
  for (let y = sorted[0][1]; y <= sorted[0][2]; y++) {
    height[y] = 1;
  }
  let sum = 0;
  for (let i = 1; i < sorted.length; i++) {
    const h = height.reduce((acc, cur) => acc + (cur === 0 ? 0 : 1), 0);
    const x2 = sorted[i][0];
    const x1 = sorted[i - 1][0];
    sum = sum + (x2 - x1) * h;

    const y1 = sorted[i][1];
    const y2 = sorted[i][2];

    for (let y = y1; y <= y2; y++) {
      height[y] += sorted[i][3];
    }
  }
  return sum;
}
