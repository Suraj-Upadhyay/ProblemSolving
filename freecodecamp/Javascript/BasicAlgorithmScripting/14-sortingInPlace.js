function getIndexToIns(arr, num) {
    let pos = 0;
    arr.push(num);
    for(let i = 1; i < arr.length; i++) {
      pos = i - 1;
      let key = arr[i]
      while (key <= arr[pos] && pos >= 0) {
        arr[pos + 1] = arr[pos];
        pos--;
      }
      arr[++pos] = key;
    }
    console.log(arr)
    return pos;
}

console.log(getIndexToIns([], 30));
