function boardGame(board, operation) {
  const dir = { U: [-1, 0], D: [1, 0], L: [0, -1], R: [0, 1] };
  let player = [0, 0];

  let score = 0;
  for (let move of operation) {
    const nextPosX = player[0] + dir[move][0];
    const nextPosY = player[1] + dir[move][1];
    if (
      nextPosX < 0 ||
      nextPosX >= board.length ||
      nextPosY < 0 ||
      nextPosY >= board.length
    ) {
      return "OUT";
    }
    score += board[nextPosX][nextPosY];
    player = [nextPosX, nextPosY];
  }
  return score;
}
