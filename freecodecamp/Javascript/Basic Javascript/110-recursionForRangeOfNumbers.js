function rangeOfNumbers(startNum, endNum) {
    if (startNum > endNum) {
      return [];
    }
    var array = rangeOfNumbers(startNum + 1, endNum);
    array.unshift(startNum);
    return array;
}

console.log(rangeOfNumbers(1, 9));
