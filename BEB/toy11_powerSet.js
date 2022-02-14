const powerSet = function (str) {
  const strSet = [...new Set(str)].sort();
  const check = Array.from({ length: strSet.length }, (v, i) => 0);
  const answer = [];

  function solution(result, p) {
    answer.push(result);

    for (let i = p; i < strSet.length; i++) {
      if (check[i] === 0) {
        check[i] = 1;
        solution(result + strSet[i], i + 1);
        check[i] = 0;
      }
    }
  }
  solution("", 0);
  return answer;
};
