const insertionSort = function (arr, callback) {
  let result = [];
  callback = callback === undefined ? (num) => num : callback;
  // 결과 배열에서 들어갈 위치를 찾고 그 위치에 넣는다

  for (let elem of arr) {
    const idx = insert(result, elem, callback);
    result = result.slice(0, idx).concat([elem]).concat(result.slice(idx));
  }

  return result;
};

function insert(arr, num, callback) {
  let index = 0;
  arr = arr.map((elem) => {
    return callback(elem);
  });
  num = callback(num);
  while (index < arr.length) {
    if (arr[index] > num) {
      return index;
    }
    index += 1;
  }
  return index;
}

console.log(insertionSort([5, 4, 3, 2, 1]));
