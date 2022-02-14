const robotPath = function (room, src, dst) {
  const dx = [0, 1, 0, -1];
  const dy = [1, 0, -1, 0];

  let q = [];
  q.push(src);
  room[src[0]][src[1]] = 1;
  while (q.length > 0) {
    now = q.shift();
    if (now[0] === dst[0] && now[1] === dst[1]) {
      return room[now[0]][now[1]] - 1;
    }
    for (let i = 0; i < 4; i++) {
      const nextX = now[0] + dx[i];
      const nextY = now[1] + dy[i];
      if (
        0 <= nextX &&
        nextX < room.length &&
        0 <= nextY &&
        nextY < room[0].length &&
        room[nextX][nextY] === 0
      ) {
        q.push([nextX, nextY]);
        room[nextX][nextY] = room[now[0]][now[1]] + 1;
      }
    }
  }
};
