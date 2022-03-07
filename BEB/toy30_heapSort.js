// 아래 코드는 수정하지 마세요.
function swap(idx1, idx2, arr) {
  [arr[idx1], arr[idx2]] = [arr[idx2], arr[idx1]];
}

function getParentIdx(idx) {
  // TODO: 여기에 코드를 작성합니다.
  return idx % 2 === 0 ? parseInt(idx / 2) - 1 : parseInt(idx / 2);
}

function insert(heap, item) {
  // TODO: 여기에 코드를 작성합니다.
  heap.push(item);
  if (heap.length === 1) {
    return heap;
  }
  let childIdx = heap.length - 1;
  let parentIdx = getParentIdx(childIdx);

  while (parentIdx >= 0 && heap[childIdx] < heap[parentIdx]) {
    swap(childIdx, parentIdx, heap);

    childIdx = parentIdx;
    parentIdx = getParentIdx(childIdx);
  }
  return heap;
}

function removeRoot(heap) {
  // TODO: 여기에 코드를 작성합니다.
  swap(0, heap.length - 1, heap);
  heap.pop();
  let root = 0;
  let lChild = 1;
  let rChild = 2;
  while (true) {
    if (heap[lChild] === undefined && heap[rChild] === undefined) {
      break;
    } else if (heap[rChild] === undefined) {
      if (heap[root] > heap[lChild]) {
        swap(root, lChild, heap);
      }
      break;
    } else {
      if (heap[root] > heap[lChild] || heap[root] > heap[rChild]) {
        const minIdx = heap[lChild] < heap[rChild] ? lChild : rChild;

        swap(root, minIdx, heap);
        root = minIdx;

        lChild = (root + 1) * 2 - 1;
        rChild = (root + 1) * 2;
      } else {
        break;
      }
    }
  }
  return heap;
}

// 아래 코드는 수정하지 마세요.
const binaryHeap = function (arr) {
  return arr.reduce((heap, item) => {
    return insert(heap, item);
  }, []);
};

const heapSort = function (arr) {
  let minHeap = binaryHeap(arr);
  // TODO: 여기에 코드를 작성합니다.
  let result = [];
  let len = minHeap.length;
  for (let i = 0; i < len; i++) {
    result[i] = minHeap[0];
    minHeap = removeRoot(minHeap);
  }
  return result;
};
let output = heapSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]);
console.log(output); // --> [1, 3, 4, 5, 10]
