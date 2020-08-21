// The operator ^ outside a character set searches
// for the pattern at the beginning.

let rickyAndCal = "Cal and Ricky both like racing.";
let calRegex = /^Cal/; // Change this line
let result = calRegex.test(rickyAndCal);

console.log(result);
