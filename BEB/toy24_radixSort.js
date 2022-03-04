function radixSort(arr) {
  const minNum = Math.min(...arr);
  const maxNum = Math.max(...arr);

  const repeatNum = Math.max(String(minNum).length, String(maxNum).length);

  console.log(minNum, maxNum, repeatNum);
  if (minNum < 0) {
    arr = arr.map((elem) => elem - minNum);
  }
  let list = [[], [], [], [], [], [], [], [], [], []];
  let rArr = [...arr];

  function digitNum(num, n) {
    let result = 0;
    if (String(num).length < n) {
      return result;
    }
    for (let i = 0; i < n; i++) {
      result = num % 10;
      num = parseInt(num / 10);
    }
    return result;
  }
  let n = 1;
  while (n <= repeatNum) {
    for (let elem of rArr) {
      list[digitNum(elem, n)].push(elem);
    }
    rArr = [];
    for (let elem of list) {
      rArr = [...rArr, ...elem];
    }
    list = [[], [], [], [], [], [], [], [], [], []];
    n++;
  }
  if (minNum < 0) {
    return rArr.map((elem) => elem + minNum);
  } else {
    return rArr;
  }
}

// minNum만큼 더했다가 마지막에 뺴준다
// 1의 자리 수 부터 진행..
// 모두가 0번에 모였을 때 종료
let output = radixSort([3, 1, 21]);
console.log(output); // --> [1, 3, 21]
