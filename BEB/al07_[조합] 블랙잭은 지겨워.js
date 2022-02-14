function boringBlackjack(cards) {
  const check = Array.from({ length: cards.length }, (v, i) => 0);
  let result = 0;
  function solution(n, num, p) {
    if (n === 3) {
      console.log(num);
      result = checkPrimeNumber(num) ? result + 1 : result;
      return;
    }

    for (let i = p; i < cards.length; i++) {
      if (check[i] === 0) {
        check[i] = 1;
        solution(n + 1, num + cards[i], i + 1);
        check[i] = 0;
      }
    }
  }
  solution(0, 0, 0);
  return result;
}

function checkPrimeNumber(num) {
  let i = 2;
  while (i <= Math.sqrt(num)) {
    if (num % i === 0) {
      return false;
    }
    i += 1;
  }
  return true;
}

let output = boringBlackjack([1, 2, 3, 4]);
console.log(output); // 1

output = boringBlackjack([2, 3, 4, 8, 13]);
console.log(output); // 3
