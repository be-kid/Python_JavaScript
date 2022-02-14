function movingStuff(stuff, limit) {
  stuff.sort((a, b) => a - b);
  let start = 0;
  let end = stuff.length - 1;
  let count = 0;

  while (start <= end) {
    if (start === end) {
      count += 1;
      break;
    }

    if (stuff[start] + stuff[end] <= limit) {
      count += 1;
      start += 1;
      end -= 1;
    } else {
      count += 1;
      end -= 1;
    }
  }

  return count;
}
