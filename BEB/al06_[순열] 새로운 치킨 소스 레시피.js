function newChickenRecipe(stuffArr, choiceNum) {
  stuffArr = stuffArr.filter((elem) => {
    const temp = elem
      .toString()
      .split("")
      .reduce((acc, cur) => {
        return (acc = cur === "0" ? acc + 1 : acc);
      }, 0);

    return temp >= 3 ? false : true;
  });
  stuffArr.sort((a, b) => a - b);
  const check = Array.from({ length: stuffArr.length }, (v, i) => 0);
  const result = [];
  function solution(n, arr) {
    if (n === choiceNum) {
      result.push(arr);
      return;
    }
    for (let i = 0; i < stuffArr.length; i++) {
      if (check[i] === 0) {
        check[i] = 1;
        solution(n + 1, [...arr, stuffArr[i]]);
        check[i] = 0;
      }
    }
  }
  solution(0, []);
  return result;
}

const output3 = newChickenRecipe([11, 1, 10, 1111111111, 10000], 4);
console.log(output3);
