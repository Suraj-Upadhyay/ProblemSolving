// Repeated patterns can be recognised with the '+' operator
// suffixed to any character.

let difficultSpelling = "Mississippi";
let myRegex = /s+/gi; // Change this line
let result = difficultSpelling.match(myRegex);
console.log(result);
