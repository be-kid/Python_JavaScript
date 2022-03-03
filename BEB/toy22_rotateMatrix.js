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

// 페어분 코드 도와줌
// const rotateMatrix = function (matrix, k) {
//   // TODO: 여기에 코드를 작성합니다.
//   k = k !== undefined ? k % 4 : 1;
//   if (matrix.length === 0 || k === 0) {
//     return matrix;
//   }
//   let m = matrix.length;
//   let n = matrix[0].length;
//   const rmatrix = [];
//   for (let row = 0; row < n; row++) {
//     rmatrix.push(Array(m).fill(0));
//   }
//   for (let i = 0; i < m; i++) {
//     for (let j = 0; j < n; j++) {
//       rmatrix[j][m - 1 - i] = matrix[i][j];
//     }
//   }

//   return rotateMatrix(rmatrix, k - 1);
// };
