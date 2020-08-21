// A group of characters may be specified to be omitted.
// This is done by preceeding the set of character
// by caret '^' operator inside a character set. for e.g. [^abdeg].

let quoteSample = "3 blind mice.";
let myRegex = /[^0-9aeiou]/gi; // Change this line
let result = quoteSample.match(myRegex); // Change this line

console.log(result);
