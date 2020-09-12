function findElement(arr, func) {
    let num = 0;
    while (num < arr.length) {
      if (func(arr[num])) return arr[num];
      num++;
    }
    return undefined;
}

console.log(findElement([1, 2, 3, 4], num => num % 2 === 0));
