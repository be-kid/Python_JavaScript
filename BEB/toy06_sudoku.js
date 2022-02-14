let board1 = [
  [0, 3, 0, 2, 6, 0, 7, 0, 1],
  [6, 8, 0, 0, 7, 0, 0, 9, 0],
  [1, 9, 0, 0, 0, 4, 5, 0, 0],
  [8, 2, 0, 1, 0, 0, 0, 4, 0],
  [0, 0, 4, 6, 0, 2, 9, 0, 0],
  [0, 5, 0, 0, 0, 3, 0, 2, 8],
  [0, 0, 9, 3, 0, 0, 0, 7, 4],
  [0, 4, 0, 0, 5, 0, 0, 3, 6],
  [7, 0, 3, 0, 1, 8, 0, 0, 0],
];
let board2 = [
  [0, 2, 0, 7, 6, 0, 0, 0, 3],
  [0, 0, 0, 0, 0, 0, 2, 0, 0],
  [9, 0, 6, 0, 2, 0, 0, 4, 0],
  [8, 0, 0, 4, 0, 0, 0, 1, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [1, 9, 0, 5, 3, 0, 6, 0, 8],
  [4, 8, 9, 0, 0, 1, 0, 3, 6],
  [0, 0, 0, 0, 5, 9, 0, 0, 0],
  [2, 1, 0, 0, 0, 0, 0, 8, 9],
];
let board3 = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [1, 2, 3, 4, 5, 6, 7, 8, 9],
];

function setRow(board) {
  return board.map((elems) => {
    const temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    elems.forEach((elem) => (temp[elem] = 1));
    return temp;
  });
}
function setColumn(board) {
  const columns = [];
  for (let i = 0; i < 9; i++) {
    const temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    for (let j = 0; j < 9; j++) {
      temp[board[j][i]] = 1;
    }
    columns.push(temp);
  }
  return columns;
}
function setSquare(board) {
  const square = [];
  const x = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
  ];
  const y = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
  ];
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      const temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
      for (let n = 0; n < 3; n++) {
        for (let m = 0; m < 3; m++) {
          temp[board[x[i][n]][y[j][m]]] = 1;
        }
      }
      square.push(temp);
    }
  }
  return square;
}

const sudoku = function (board) {
  const rows = setRow(board);
  const columns = setColumn(board);
  const squares = setSquare(board);
  let flag = true;
  let result;
  function solution(n) {
    if (n === 81) {
      flag = false;
      result = board;
      console.log(result);
      return;
    } else {
      const x = parseInt(n / 9);
      const y = n % 9;
      if (board[x][y] === 0) {
        for (let i = 1; i <= 9; i++) {
          if (
            rows[x][i] === 0 &&
            columns[y][i] === 0 &&
            squares[parseInt(x / 3) * 3 + parseInt(y / 3)][i] === 0
          ) {
            rows[x][i] = 1;
            columns[y][i] = 1;
            squares[parseInt(x / 3) * 3 + parseInt(y / 3)][i] = 1;
            board[x][y] = i;
            solution(n + 1);
            if (flag === false) {
              break;
            }
            rows[x][i] = 0;
            columns[y][i] = 0;
            squares[parseInt(x / 3) * 3 + parseInt(y / 3)][i] = 0;
            board[x][y] = 0;
          }
        }
      } else {
        solution(n + 1);
      }
    }
  }

  solution(0);
  return board;
};

sudoku(board3);
