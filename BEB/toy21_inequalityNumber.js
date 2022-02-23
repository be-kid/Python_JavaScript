const inequalityNumber = function (signs) {
  signs = signs.split(" ");

  const check = Array(10).fill(false);

  let maxNum = 0;
  let minNum = 9876543210;
  function pickNumber(nums) {
    if (nums.length === signs.length + 1) {
      // 합쳐서 최소, 최대 숫자와 비교, 교환
      const joinNum = nums.reduce((acc, cur) => {
        return (acc = acc * 10 + cur);
      });
      maxNum = maxNum < joinNum ? joinNum : maxNum;
      minNum = minNum > joinNum ? joinNum : minNum;
      return;
    }
    for (let i = 0; i < 10; i++) {
      if (!check[i]) {
        // 아직 고르지 않은 숫자고
        if (nums.length === 0) {
          //아직 한개도 안골랐으면 부등호 확인 필요 없음
          check[i] = true;
          pickNumber([...nums, i]);
          check[i] = false;
        } else {
          // 부등호 확인 필요, 자기 앞 숫자와 부등호를 확인
          const currentIdx = nums.length - 1;
          if (signs[currentIdx] === ">" && nums[currentIdx] > i) {
            check[i] = true;
            pickNumber([...nums, i]);
            check[i] = false;
          } else if (signs[currentIdx] === "<" && nums[currentIdx] < i) {
            check[i] = true;
            pickNumber([...nums, i]);
            check[i] = false;
          }
        }
      }
    }
  }

  pickNumber([]);
  return maxNum - minNum;
};

// 부등호의 개수 + 1개 만큼 숫자가 필요함
// 숫자를 무작정 다 고르지 말고 부등호를 넣었을 때 만족하는지 확인하고 고르기
// 백트레킹
let output = inequalityNumber("<");
console.log(output); // --> 88 (89 - 01)

output = inequalityNumber("< >");
console.log(output); // --> 876 (897 - 021)

output = inequalityNumber("> < >");
console.log(output); // --> 8,754 (9,786 - 1,032)
