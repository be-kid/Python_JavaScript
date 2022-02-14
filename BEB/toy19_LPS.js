const LPS = function (str) {
  let start = 0;
  let end = str.length - 1;
  let result = 0;

  while (start < end) {
    const front = str.slice(0, start + 1);
    const back = str.slice(end, str.length);
    if (front === back) {
      result = front.length;
    }
    start += 1;
    end -= 1;
  }
  return result;
};
