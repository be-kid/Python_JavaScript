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

// 1. num?????? ?????? ??????
//      1) 2??? ?????? ??????
//      2) ?????? ?????? (????????????)
// 2. ??????????????? ??? ???????????? ?????? 2??? ???????????? ?????? ????????? ????????? ??????
//      1) ????????? ???????????? ??????????????? ???????????? ?????? ??????.
//      2) 1??? ????????? ?????? ??????????????? ?????? ?????? ??? ?????? 1??? 2??? ??????????????? ??????
//      3) ?????? 1??? 2??? ??????????????? ??????
//      4) ????????? ??????
// 3. ????????? ???????????? ?????? ?????? ??????
// 4. 1??? ????????? ?????? ????????? ??????, ?????? ????????? ??? ?????? ????????? ??????

let village = [
  "0022", // ??? ?????? ???
  "0020",
  "0020",
  "0220",
];
let num = 1;
let output = gossipProtocol2(village, num);
console.log(output); // --> 0 (?????? ?????? ????????? ????????? ?????? ?????? ??????)

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
????????? ????????? ????????? ?????? N??? ????????? ????????? ????????? ??????????????????. 
'0'??? ????????? ?????? ?????? ??? ?????? ????????????, '1'??? ????????? ????????? ?????? ?????? ?????? ????????????, 
'2'??? ????????? ?????? ?????? ???????????? ?????? ????????? ????????? ?????? ?????? ?????? ???????????????. 
??? ????????? ??????????????? ???????????? ???????????? ?????? ?????? ?????? ???????????? ?????? ????????? ?????? ??? 
????????? ?????? ?????? ???????????? ??????????????? ?????????. ??? ??????????????? ??? ?????? ???, 
????????? ???????????? ??? ??? ?????? ?????? ?????? ????????? ???????????? ???????????????. 
????????? ???????????? ?????? ?????? ??? ?????? ???, ???????????? ??? ??? ?????? ?????? ?????? ????????? ?????? ????????? ???????????????. 
???, ?????? ?????? ???????????? ???????????? ?????? ??????('2')??? ?????? ????????? ?????? ????????? ???????????? ????????????. 
?????? ?????? ???????????? ????????? ??? ?????? ?????????(num)??? ????????? ???, 
?????? ????????? ????????? ???????????? ??? ?????? ?????? ????????? ???????????? ?????????.

??????
?????? 1 : village
string ????????? ????????? ?????? ??????
village.length??? village[i].length??? 50 ??????
village[i]??? string ??????
village[i][j]??? ????????? i, ????????? j??? ????????? ????????? ??????
village[i][j]??? '0', '1' ?????? '2'
?????? 2: num
number ????????? 10 ????????? ?????? ??????
?????? ?????? ???????????? ??????????????? ?????? ???
??????
number ????????? ???????????? ?????????.
????????????
?????? ?????? ?????? ???????????? ?????? ?????? ????????????.
?????? ?????? ???????????? ???????????? ?????? ??????(???2???)??? ????????? ???????????? ????????????.
?????? ?????? ???????????? ?????? ????????? ??????('2')??? ?????? 10 ???????????????.
village??? ???????????? ???????????? ????????? ???????????????.
*/
