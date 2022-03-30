function longestPalindrome(str) {
  if (str.length < 2) return str.length;

  const LENGTH = str.length;
  const isPalindrome = Array(LENGTH)
    .fill(false)
    .map((_) => Array(LENGTH).fill(false));

  let maxLen = 1;
  for (let i = 0; i < LENGTH; i++) {
    isPalindrome[i][i] = true;
  }

  for (let i = 0; i < LENGTH - 1; i++) {
    if (str[i] === str[i + 1]) {
      isPalindrome[i][i + 1] = true;
      maxLen = 2;
    }
  }

  for (let len = 3; len <= LENGTH; len++) {
    for (let startIdx = 0; startIdx <= LENGTH - len; startIdx++) {
      const endIdx = startIdx + len - 1;
      if (
        isPalindrome[startIdx + 1][endIdx - 1] === true &&
        str[startIdx] === str[endIdx]
      ) {
        isPalindrome[startIdx][endIdx] = true;
        maxLen = len;
      }
    }
  }
  return maxLen;
}

let str = "My dad is a racecar athlete";
let result = longestPalindrome(str);
console.log(result); // --> 11 ('a racecar a')

str = " dad ";
result = longestPalindrome(str);
console.log(result); // --> 5 (' dad ')
