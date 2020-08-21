// \w = [A-Za-z0-9_] : Shorthand character classes.

let quoteSample = "The five boxing wizards jump quickly.";
let alphabetRegexV2 = /\w/gi; // Change this line
let result = quoteSample.match(alphabetRegexV2).length;

console.log(result); // Returns the count of alphanumeric character in the string.
