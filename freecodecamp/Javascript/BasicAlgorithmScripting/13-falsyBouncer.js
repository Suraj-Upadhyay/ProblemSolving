function bouncer(arr) {
    let retArr = [];
    for (let i = 0; i < arr.length; i++) {
      if (Boolean(arr[i])) retArr.push(arr[i]);
    }
    return retArr;
}

console.log(bouncer([7, "ate", "", false, 9]));
