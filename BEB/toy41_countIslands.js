const countIslands = function (grid) {
  const visited = Array.from({ length: grid.length }, (v) => {
    return Array.from({ length: grid[0].length }, (v) => 0);
  });

  const queue = [];
  const dx = [0, 1, -1, 0];
  const dy = [1, 0, 0, -1];
  let result = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === "1" && visited[i][j] === 0) {
        queue.push([i, j]);
        visited[i][j] = 1;
        result += 1;
        while (queue.length > 0) {
          const now = queue.shift();

          for (let k = 0; k < 4; k++) {
            const nx = now[0] + dx[k];
            const ny = now[1] + dy[k];
            if (
              nx >= 0 &&
              nx < grid.length &&
              ny >= 0 &&
              ny < grid[0].length &&
              grid[nx][ny] === "1" &&
              visited[nx][ny] === 0
            ) {
              queue.push([nx, ny]);
              visited[nx][ny] = 1;
            }
          }
        }
      }
    }
  }
  console.log(visited);
  return result;
};

let grid = [
  ["0", "1", "1", "1"],
  ["0", "1", "1", "1"],
  ["1", "1", "0", "0"],
];
let result = countIslands(grid);
console.log(result); // --> 1

grid = [
  ["0", "1", "1", "1", "0"],
  ["0", "1", "0", "0", "0"],
  ["0", "0", "0", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "1", "0"],
];
result = countIslands(grid);
console.log(result); // --> 3
