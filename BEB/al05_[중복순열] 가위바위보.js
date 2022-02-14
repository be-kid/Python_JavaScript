function rockPaperScissors(rounds) {
  rounds = rounds === undefined ? 3 : rounds;
  const check = [0, 0, 0];
  const rps = { 0: "rock", 1: "paper", 2: "scissors" };
  const result = [];
  function solution(n, arr) {
    if (n === rounds) {
      result.push(arr);
      return;
    }
    for (let i = 0; i < 3; i++) {
      if (check[i] < rounds) {
        check[i] += 1;
        solution(n + 1, [...arr, rps[i]]);
        check[i] -= 1;
      }
    }
  }

  solution(0, []);
  return result;
}

console.log(rockPaperScissors());
