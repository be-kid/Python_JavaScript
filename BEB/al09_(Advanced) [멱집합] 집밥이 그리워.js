function missHouseMeal(sideDishes) {
  sideDishes.sort();
  const check = Array.from({ length: sideDishes.length }, (v, i) => 0);
  const result = [];
  function solution(arr, p) {
    result.push(arr);

    for (let i = p; i < sideDishes.length; i++) {
      if (check[i] === 0) {
        check[i] = 1;
        solution([...arr, sideDishes[i]], i + 1);
        check[i] = 0;
      }
    }
  }
  solution([], 0);

  return result;
}

console.log(missHouseMeal(["egg", "fish", "kim"]));
