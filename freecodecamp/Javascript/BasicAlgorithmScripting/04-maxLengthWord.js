function findLongestWordLength(str) {
    let max = -1
    let regex = /\w+/gi;
    let array = str.match(regex);
    for (let i = 0; i < array.length; i++){
      if (max < array[i].length)
        max = array[i].length;
    }
    return max;
}

let response = findLongestWordLength("The quick brown fox jumped over the lazy dog");

console.log(response);
