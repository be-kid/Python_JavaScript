function partTimeJob(k) {
  const coins = [500, 100, 50, 10, 5, 1];
  let count = 0;
  for (let coin of coins) {
    count = count + parseInt(k / coin);
    k = k - coin * parseInt(k / coin);
  }
  return count;
}
