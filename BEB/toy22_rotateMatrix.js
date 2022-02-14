const rotateMatrix = function (matrix, rotate) {
  let newMatrix = [];
  rotate = rotate ?? 1;
  rotate = rotate % 4;
  let row = matrix.length;
  let column = matrix.length === 0 ? 0 : matrix[0].length;

  for (let r = 0; r < rotate; r++) {
    newMatrix = [];
    for (let j = 0; j < column; j++) {
      let temp = [];
      for (let i = row - 1; i >= 0; i--) {
        temp.push(matrix[i][j]);
      }
      newMatrix.push(temp);
    }
    matrix = [...newMatrix];
    [row, column] = [column, row];
  }

  return newMatrix;
};

// rotate를 4로 나눈 나머지
