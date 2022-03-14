const createMatrix = (village) => {
  const matrix = [];
  village.forEach((line) => {
    const row = [];
    for (let i = 0; i < line.length; i++) row.push(line[i]);
    matrix.push(row);
  });
  return matrix;
};

const countHouse = (village) => {
  let count1 = 0;
  let count2 = 0;
  let pos = [];
  for (let i = 0; i < village.length; i++) {
    for (let j = 0; j < village[0].length; j++) {
      count1 = village[i][j] === "1" ? count1 + 1 : count1;
      count2 = village[i][j] === "2" ? count2 + 1 : count2;
      if (village[i][j] === "2") {
        pos.push([i, j]);
      }
    }
  }
  return [count1, count2, pos];
};

const spread = (village, agentHouses, normalHouseNum) => {
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  const visited = [];
  village.forEach((line) => {
    const row = [];
    for (let i = 0; i < line.length; i++) row.push(line[i] === "2" ? 1 : 0);
    visited.push(row);
  });
  const queue = [...agentHouses];
  let front = 0;

  let time = Infinity;
  while (queue.length > front) {
    let cur = queue[front];
    front += 1;
    for (let i = 0; i < 4; i++) {
      const nx = cur[0] + dx[i];
      const ny = cur[1] + dy[i];
      if (0 <= nx && nx < village.length && 0 <= ny && ny < village[0].length) {
        if (visited[nx][ny] === 0 && village[nx][ny] === "1") {
          visited[nx][ny] = visited[cur[0]][cur[1]] + 1;
          queue.push([nx, ny]);
          normalHouseNum -= 1;
          time = visited[nx][ny];
        }
      }
    }
  }
  if (normalHouseNum === 0) {
    return time - 1;
  } else {
    return Infinity;
  }
};

const gossipProtocol2 = function (village, num) {
  const [normalHouseNum, emergencyHouseNum, agentCandidateHouses] =
    countHouse(village);

  if (normalHouseNum === 0) {
    return 0;
  }
  let result = Infinity;
  const checked = Array(emergencyHouseNum).fill(0);
  const selectAgents = (n, p) => {
    if (n === num) {
      const time = spread(
        createMatrix(village),
        agentCandidateHouses.filter((elem, idx) => {
          return checked[idx] === 1;
        }),
        normalHouseNum
      );
      result = result > time ? time : result;
      return;
    }
    for (let i = p; i < emergencyHouseNum; i++) {
      if (checked[i] === 0) {
        checked[i] = 1;
        selectAgents(n + 1, i + 1);
        checked[i] = 0;
      }
    }
  };
  selectAgents(0, 0);
  return result;
};

// 1. num개의 대표 선정
//      1) 2의 위치 체크
//      2) 요원 선정 (백트래킹)
// 2. 선정되었을 때 선정되지 않은 2를 제외하고 모두 확산이 되는지 확인
//      1) 선정된 요원들을 시작점으로 너비우선 탐색 진행.
//      2) 1의 개수도 미리 구해뒀다가 확산 종료 후 모든 1이 2로 바뀌었는지 체크
//      3) 모든 1이 2로 바뀌었다면 성공
//      4) 아니면 실패
// 3. 확산에 성공했을 경우 시간 기록
// 4. 1로 돌아가 다른 경우도 실행, 모든 경우를 다 해서 최소값 출력

let village = [
  "0022", // 첫 번째 줄
  "0020",
  "0020",
  "0220",
];
let num = 1;
let output = gossipProtocol2(village, num);
console.log(output); // --> 0 (이미 모든 주민이 정보를 알고 있는 상태)

village = [
  "1001212",
  "1201011",
  "1102001",
  "2111102",
  "0012111",
  "1111101",
  "2121102",
];
num = 5;
output = gossipProtocol2(village, num);
console.log(output); // --> 3

/*
세로와 가로의 길이가 모두 N인 마을의 지도가 배열로 주어졌습니다. 
'0'은 주민이 살지 않는 빈 땅을 의미하고, '1'은 평범한 주민이 살고 있는 집을 의미하며, 
'2'는 유사시 비상 연락 요원으로 선정 가능한 주민이 살고 있는 집을 의미합니다. 
이 마을의 비상연락망 시스템을 구축하기 위해 비상 연락 요원으로 선정 가능한 주민 중 
일부를 비상 연락 요원으로 임명하려고 합니다. 각 담당자들은 한 시간 후, 
정보를 상하좌우 한 칸 바로 옆에 있는 집으로 전달하기 시작합니다. 
정보를 전달받은 주민 역시 한 시간 후, 상하좌우 한 칸 바로 옆에 있는 집으로 해당 정보를 전달합니다. 
단, 비상 연락 요원으로 선정받지 못한 주민('2')은 이에 불만을 품고 정보를 전달하지 않습니다. 
비상 연락 요원으로 지정할 수 있는 최대수(num)가 주어질 때, 
마을 전체로 정보가 전달되는 데 가장 빠른 시간을 리턴해야 합니다.

입력
인자 1 : village
string 타입을 요소로 갖는 배열
village.length와 village[i].length는 50 이하
village[i]는 string 타입
village[i][j]는 세로로 i, 가로로 j인 지점의 정보를 의미
village[i][j]는 '0', '1' 또는 '2'
인자 2: num
number 타입의 10 이하의 양의 정수
비상 연락 요원으로 지정가능한 최대 수
출력
number 타입을 리턴해야 합니다.
주의사항
모든 집이 전부 연결되어 있는 것은 아닙니다.
비상 연락 요원으로 선택되지 않은 주민(‘2’)은 정보를 전달하지 않습니다.
비상 연락 요원으로 선정 가능한 주민('2')의 수는 10 이하입니다.
village를 그래프로 구현하는 함수가 주어집니다.
*/
