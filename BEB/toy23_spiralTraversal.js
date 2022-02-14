const spiralTraversal = function (matrix) {
  const dir = {
    0: [0, 1],
    1: [1, 0],
    2: [0, -1],
    3: [-1, 0],
  };
  const check = Array.from({ length: matrix.length }, () =>
    Array.from({ length: matrix[0].length }, () => 0)
  );

  let pos = [0, 0];
  let curDir = 0;
  let result = "";
  while (true) {
    result += matrix[pos[0]][pos[1]];
    if (result.length === matrix.length * matrix[0].length) {
      break;
    }
    check[pos[0]][pos[1]] = 1;
    let nextPos = [pos[0] + dir[curDir][0], pos[1] + dir[curDir][1]];
    if (
      nextPos[0] >= 0 &&
      nextPos[0] < matrix.length &&
      nextPos[1] >= 0 &&
      nextPos[1] < matrix[0].length &&
      check[nextPos[0]][nextPos[1]] === 0
    ) {
      pos = [...nextPos];
    } else {
      curDir = (curDir + 1) % 4;
      pos = [pos[0] + dir[curDir][0], pos[1] + dir[curDir][1]];
    }
  }
  return result;
};

let matrix = [
  ["A", "B", "C"],
  ["D", "E", "F"],
  ["G", "H", "I"],
];
let output = spiralTraversal(matrix);
console.log(output); // --> 'ABCFIHGDE'

matrix = [
  ["T", "y", "r", "i"],
  ["i", "s", "t", "o"],
  ["n", "r", "e", "n"],
  ["n", "a", "L", " "],
];
output = spiralTraversal(matrix);
console.log(output); // --> 'Tyrion Lannister'
