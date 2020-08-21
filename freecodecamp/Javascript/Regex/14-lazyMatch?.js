// Regexes by default perform greedy match i.e. returning the
// longest possible string fitting the pattern.
// To make the regex return the shortest string fitting the character
// use the '?' operator. And this is called lazy match.

let text = "<h1>Winter is coming</h1>";
let myRegex = /<.*?>/; // Change this line
let result = text.match(myRegex);

console.log(result); // Only match <h1>
