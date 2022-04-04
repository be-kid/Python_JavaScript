// 좌표평면 위의 두 점 사이의 거리를 계산하는 함수입니다.
function calculateDistance(p1, p2) {
  const yDiffSquared = Math.pow(p2[0] - p1[0], 2);
  const xDiffSquared = Math.pow(p2[1] - p1[1], 2);
  const dist = Math.sqrt(yDiffSquared + xDiffSquared);
  return Math.floor(dist * 100);
}

const TSP = function (places) {
  // TODO: 여기에 코드를 작성합니다.
  const visited = Array(places.length).fill(0);

  let result = Number.MAX_SAFE_INTEGER;

  function solution(n, prePos, dist) {
    if (n === places.length) {
      result = result > dist ? dist : result;
      return;
    }

    for (let i = 0; i < places.length; i++) {
      if (visited[i] === 0) {
        visited[i] = 1;
        solution(n + 1, i, dist + calculateDistance(places[prePos], places[i]));
        visited[i] = 0;
      }
    }
  }

  for (let i = 0; i < places.length; i++) {
    solution(0, i, 0);
  }

  return result;
};

let placesToVisit = [
  [0, 0],
  [1, 1],
  [1, 3],
  [2, 2],
];
let output = TSP(placesToVisit);
console.log(output); // --> 423
// 방문 순서: [0, 0], [1, 1], [2, 2], [1, 3]

placesToVisit = [
  [0, 0],
  [3, 3],
  [-3, 3],
  [2, 3],
  [1, 3],
];
output = TSP(placesToVisit);
console.log(output); // --> 940
// 방문 순서: [-3, 3], [1, 3], [2, 3], [3, 3], [0, 0]
