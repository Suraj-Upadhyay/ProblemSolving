function frankenSplice(arr1, arr2, n) {
    return arr2.slice(0, n).concat(arr1).concat(arr2.slice(n, arr2.length));
}

console.log(frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2));

// Returns [ 'head', 'shoulders', 'claw', 'tentacle', 'knees', 'toes' ]