function mutation(arr) {
    for (let i = 0; i < arr[1].length; i++)
      if ((arr[0].indexOf(arr[1][i].toUpperCase()) == -1) && (arr[0].indexOf(arr[1][i].toLowerCase()) == -1))
        return false;
    return true;
}

console.log(mutation(["hello", "hey"]));
