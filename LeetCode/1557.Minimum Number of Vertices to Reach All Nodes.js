/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findSmallestSetOfVertices = function (n, edges) {
  let g = Array.from({ length: n }, () => 0);

  for (let edge of edges) {
    g[edge[1]] += 1;
  }

  let result = [];
  for (let i = 0; i < n; i++) {
    if (g[i] === 0) {
      result.push(i);
    }
  }
  return result;
};
