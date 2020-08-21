// Character classes are defined with a bracket enclosing
// a group of characters to be recognized for a single place.

let quoteSample = "Beware of bugs in the above code; I have only proved it correct, not tried it.";
let vowelRegex = /[aeiou]/gi; // Change this line
let result = quoteSample.match(vowelRegex); // Change this line

console.log(result);
