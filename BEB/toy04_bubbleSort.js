const bubbleSort = function (arr) {
  let flag = false;
  for (let i = 0; i < arr.length; i++) {
    flag = true;
    for (let j = 0; j < arr.length - i; j++) {
      let temp;
      if (arr[j] > arr[j + 1]) {
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
        flag = false;
      }
    }
    if (flag) {
      break;
    }
  }
  return arr;
};
