// Filter all the sub-arrays of arr such that none contains the element elem.
function filteredArray(arr, elem) {
    let newArr = [];
    // Only change code below this line
    for (let i = 0; i < arr.length; i++) {
      newArr.push(arr[i]);
      for (let j = 0; j < arr[i].length; j++)
        if (arr[i][j] === elem) newArr.pop();
    }
    // Only change code above this line
    return newArr;
}

console.log(filteredArray([[3, 2, 3], [1, 6, 3], [3, 13, 26], [19, 3, 9]], 3));
