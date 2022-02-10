var allPathsSourceTarget = function (graph) {
  let result = [];

  let check = Array.from({ length: graph.length }, () => 0);

  function solution(now, paths) {
    if (now === graph.length - 1) {
      result.push(paths);
    }

    for (let i = 0; i < graph[now].length; i++) {
      let nextPos = graph[now][i];
      if (check[nextPos] === 0) {
        check[nextPos] = 1;
        solution(nextPos, paths.concat([nextPos]));
        check[nextPos] = 0;
      }
    }
  }

  solution(0, [0]);

  return result;
};
