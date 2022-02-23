const getItemFromTwoSortedArrays = function (arr1, arr2, k) {
  let leftIdx = 0,
    rightIdx = 0;

  while (k > 0) {
    let cnt = Math.ceil(k / 2);
    let leftStep = cnt,
      rightStep = cnt;
    console.log("count", cnt);
    if (leftIdx === arr1.length) {
      rightIdx = rightIdx + k;
      break;
    }
    if (rightIdx === arr2.length) {
      leftIdx = leftIdx + k;
      break;
    }

    if (cnt > arr1.length - leftIdx) leftStep = arr1.length - leftIdx;
    if (cnt > arr2.length - rightIdx) rightStep = arr2.length - rightIdx;

    if (arr1[leftIdx + leftStep - 1] < arr2[rightIdx + rightStep - 1]) {
      leftIdx = leftIdx + leftStep;
      k = k - leftStep;
    } else {
      rightIdx = rightIdx + rightStep;
      k = k - rightStep;
    }
  }
  leftMax = arr1[leftIdx - 1] || -1;
  rightMax = arr2[rightIdx - 1] || -1;
  return Math.max(leftMax, rightMax);
};

// const getItemFromTwoSortedArrays = function (arr1, arr2, k) {
//   let start1 = 0;
//   let end1 = arr1.length < k ? arr1.length - 1 : k - 1;
//   let start2 = 0;
//   let end2 = arr2.length < k ? arr2.length - 1 : k - 1;
//   arr1[end1 + 1] = Infinity;
//   arr2[end2 + 1] = Infinity;

//   let count = 0;
//   while (true) {
//     let mid1;
//     let mid2;
//     if (start1 >= end1 || mid1 === start1) {
//       mid1 = start1;
//     } else {
//       mid1 =
//         (start1 + end1) % 2 === 0
//           ? parseInt((start1 + end1) / 2) - 1
//           : parseInt((start1 + end1) / 2);
//     }
//     if (start2 >= end2 || mid2 === start2) {
//       mid2 = start2;
//     } else {
//       mid2 =
//         (start2 + end2) % 2 === 0
//           ? parseInt((start2 + end2) / 2) - 1
//           : parseInt((start2 + end2) / 2);
//     }
//     //console.log(start1, mid1, end1, start2, mid2, end2);
//     if (arr1[mid1] < arr2[mid2]) {
//       count = count + mid1 - start1 + 1;
//       start1 = mid1 + 1;
//       if (count === k) {
//         return arr1[mid1];
//       }
//       if (start1 >= end1 || mid1 === start1) {
//         mid1 = start1;
//       } else {
//         mid1 =
//           (start1 + end1) % 2 === 0
//             ? parseInt((start1 + end1) / 2) - 1
//             : parseInt((start1 + end1) / 2);
//       }
//     }
//     if (arr1[mid1] >= arr2[mid2]) {
//       count = count + mid2 - start2 + 1;
//       start2 = mid2 + 1;
//       if (count === k) {
//         return arr2[mid2];
//       }
//       if (start2 >= end2 || mid2 === start2) {
//         mid2 = start2;
//       } else {
//         mid2 =
//           (start2 + end2) % 2 === 0
//             ? parseInt((start2 + end2) / 2) - 1
//             : parseInt((start2 + end2) / 2);
//       }
//     }
//   }
// };

// k번째 요소가 무엇이냐....
// 그냥 단순하게 하나씩 빼내면 O(n)
// 일단 양 배열에서 k번째 이후로는 필요없으니까 잘라냄.
// 근데 배열 길이가 k보다 작을 수도 있으니까 체크

let arr1 = [1, 3, 5, 7, 9];
let arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 1);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 2);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 3);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 4);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 5);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 6);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 7);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 8);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 9);
console.log(result);
arr1 = [1, 3, 5, 7, 9];
arr2 = [2, 4, 6, 8, 10];
result = getItemFromTwoSortedArrays(arr1, arr2, 10);
console.log(result);

arr1 = [1, 4, 8, 10];
arr2 = [2, 3, 5, 9];
result = getItemFromTwoSortedArrays(arr1, arr2, 5);
console.log(result);

arr1 = [1, 1, 2, 10];
arr2 = [2, 3, 7, 12];
result = getItemFromTwoSortedArrays(arr1, arr2, 7);
console.log(result);
