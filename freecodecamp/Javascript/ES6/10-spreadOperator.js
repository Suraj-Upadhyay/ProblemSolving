// The spread operator unpacks an array into comma separated numbers `...arr`.
// The spread operator works in-place, linke in an argument or array literal.

const arr1 = ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
let arr2;

arr2 = [...arr1];  // Change this line

console.log(arr2);
// Outputs: [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY' ]
