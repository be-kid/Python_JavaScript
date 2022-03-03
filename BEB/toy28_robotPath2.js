const robotPath2 = function (room, src, sDir, dst, dDir) {
  const move = { 1: [-1, 0], 2: [0, 1], 3: [1, 0], 4: [0, -1] };
  const w = room[0].length;
  const h = room.length;
  const queue = [src];

  const isValid = (x, y) => {
    return 0 <= x && x < h && 0 <= y && y < w;
  };

  const directions = [];
  const dist = [];
  for (let row = 0; row < h; row++) {
    directions.push(Array(w).fill(0));
    dist.push(Array(w).fill(Number.MAX_SAFE_INTEGER));
  }
  directions[src[0]][src[1]] = sDir;
  dist[src[0]][src[1]] = 0;

  while (queue.length > 0) {
    const [curX, curY] = queue.shift();
    const curDir = directions[curX][curY];

    for (let nextDir = 1; nextDir < 5; nextDir++) {
      const nextX = curX + move[nextDir][0];
      const nextY = curY + move[nextDir][1];

      if (isValid(nextX, nextY) === false || room[nextX][nextY] === 1) continue;

      const dDiff = Math.abs(nextDir - curDir);
      let candidate;
      if (dDiff === 0) {
        candidate = dist[curX][curY] || 1;
      } else if (dDiff === 2) {
        candidate = dist[curX][curY] + 3;
      } else {
        candidate = dist[curX][curY] + 2;
      }

      if (nextX === dst[0] && nextY === dst[1]) {
        const dDiff = Math.abs(nextDir - dDir);
        if (dDiff === 0) {
          candidate = candidate;
        } else if (dDiff === 2) {
          candidate = candidate + 2;
        } else {
          candidate = candidate + 1;
        }
      }

      if (candidate < dist[nextX][nextY]) {
        queue.push([nextX, nextY]);
        dist[nextX][nextY] = candidate;
        directions[nextX][nextY] = nextDir;
      }
    }
  }
  console.log(dist);
  return dist[dst[0]][dst[1]];
};
let room = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 1, 1],
];
let src = [3, 0];
let sDir = 3;
let dst = [2, 2];
let dDir = 2;
let output = robotPath2(room, src, sDir, dst, dDir);
console.log(output); // --> 11

room = [
  [0, 0, 0, 0, 0, 0],
  [0, 1, 1, 0, 1, 0],
  [0, 1, 0, 0, 0, 0],
  [0, 0, 1, 1, 1, 0],
  [1, 0, 0, 0, 0, 0],
];
src = [4, 2];
sDir = 1;
dst = [2, 2];
dDir = 3;
output = robotPath2(room, src, sDir, dst, dDir);
console.log(output); // --> 7
