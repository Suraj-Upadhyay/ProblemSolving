// The third argument to splice is a variable length argument which
// takes takes the elements to be added at the specified index,

function htmlColorNames(arr) {
    // Only change code below this line
    arr.splice(0, 2, "DarkSalmon", "BlanchedAlmond");
    // Only change code above this line
    return arr;
}

console.log(htmlColorNames(['DarkGoldenRod', 'WhiteSmoke', 'LavenderBlush', 'PaleTurquoise', 'FireBrick']));

// [ 'DarkSalmon',
//   'BlanchedAlmond',
//   'LavenderBlush',
//   'PaleTurquoise',
//   'FireBrick' ]
