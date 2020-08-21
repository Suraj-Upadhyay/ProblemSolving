// Note: The string calls the match method and
// the regex is passed as an argument.

let extractStr = "Extract the word 'coding' from this string.";
let codingRegex = /coding/; // Change this line
let result = extractStr.match(codingRegex); // Change this line

console.log(result);

// [ 'coding',
//   index: 18,
//   input: 'Extract the word \'coding\' from this string.',
//   groups: undefined ]
