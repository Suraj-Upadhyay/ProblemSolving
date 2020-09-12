function chunkArrayInGroups(arr, size) {
    if (size <= 0) return arr;
    let retArray = [];
    let i = 0;
    while (i < arr.length) {
      retArray.push(arr.slice(i, i + size));
      i += size;
    }
    if (i > arr.length) {
      retArray.concat([arr.slice(i - size, arr.length)]);
    }
    return retArray;
}

console.log(chunkArrayInGroups(["a", "b", "c", "d"], 2));
