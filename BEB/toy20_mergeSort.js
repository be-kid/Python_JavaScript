const mergeSort = function (arr) {
  if (arr.length < 2) {
    return arr;
  }
  let left = mergeSort(arr.slice(0, parseInt(arr.length / 2)));
  let right = mergeSort(arr.slice(parseInt(arr.length / 2)));

  let newArr = [];
  while (left.length > 0 && right.length > 0) {
    if (left[0] < right[0]) {
      newArr.push(left.shift());
    } else {
      newArr.push(right.shift());
    }
  }
  if (left.length === 0) {
    return newArr.concat(right);
  } else {
    return newArr.concat(left);
  }
};

console.log(mergeSort([4, 7, 4, 3, 9, 1, 2]));
