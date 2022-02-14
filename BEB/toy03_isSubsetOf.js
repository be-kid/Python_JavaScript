const isSubsetOf = function (base, sample) {
  const nums = {};
  base.forEach((elem) => (nums[elem] = 1));

  for (let elem of sample) {
    if (!nums[elem]) {
      return false;
    }
  }

  return true;
};
