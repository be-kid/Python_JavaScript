const createMatrix = (village) => {
  const matrix = [];
  village.forEach((line) => {
    const row = [];
    for (let i = 0; i < line.length; i++) row.push(line[i]);
    matrix.push(row);
  });
  return matrix;
};
let result = 0;
const gossipProtocol = function (village, row, col) {
  const dx = [0, 1, 0, -1];
  const dy = [-1, 0, 1, 0];
  let graph = createMatrix(village);
  let q = [[row, col]];
  graph[row][col] = 0;
  while (q.length > 0) {
    now = q.shift();
    for (let i = 0; i < 4; i++) {
      const nextX = now[0] + dx[i];
      const nextY = now[1] + dy[i];
      if (
        0 <= nextX &&
        nextX < graph.length &&
        0 <= nextY &&
        nextY < graph[0].length &&
        graph[nextX][nextY] === "1"
      ) {
        q.push([nextX, nextY]);
        graph[nextX][nextY] = graph[now[0]][now[1]] + 1;
        result = graph[nextX][nextY];
      }
    }
  }
  return result;
};
