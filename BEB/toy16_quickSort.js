const quickSort = function (arr, callback) {
  if (arr.length < 2) {
    return arr;
  }

  callback =
    callback ??
    function (num) {
      return num;
    };

  let left = [];
  let right = [];
  let pivot = arr[arr.length - 1];
  for (let i = 0; i < arr.length - 1; i++) {
    console.log(callback(pivot), callback(arr[i]));
    callback(pivot) < callback(arr[i]) ? right.push(arr[i]) : left.push(arr[i]);
  }
  return quickSort(left, callback)
    .concat([pivot])
    .concat(quickSort(right, callback));
};

let output = quickSort([3, 1, 21]);
console.log(output); // --> [1, 3, 21]

output = quickSort([-11, -10, 2, 29], (item) => item * item);
console.log(output);
