// The opposite of character set shortchut \w is \W.
// i.e. \W = [^\w] = [^A-Za-z0-9_]

let quoteSample = "The five boxing wizards jump quickly.";
let nonAlphabetRegex = /\W/g; // Change this line
let result = quoteSample.match(nonAlphabetRegex).length;

console.log(result);
