const subsetSum = function (set, bound) {
  let max = 0;

  const cached = Array(300 + 1).fill(false);
  set.forEach((member) => {
    const reachables = [];

    for (let wanted = 1; wanted <= bound - member; wanted++) {
      if (cached[wanted] === true) {
        const reached = wanted + member;
        reachables.push(reached);
        if (reached > max) max = reached;
      }
    }

    reachables.forEach((r) => (cached[r] = true));

    if (member <= bound) {
      cached[member] = true;
      if (member > max) max = member;
    }
  });
  return max;
};

let output = subsetSum([1, 8, 3, 15], 10);
console.log(output); // --> 9 (= 1 + 8)

output = subsetSum([20, 80, 99, 27, 35], 100);
console.log(output); // --> 100 (= 20 + 80)

output = subsetSum([10, 20, 15, 25, 30], 5);
console.log(output); // --> 0
