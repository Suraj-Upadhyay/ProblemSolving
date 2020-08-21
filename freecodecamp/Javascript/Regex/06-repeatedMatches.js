// To make the match method return all instances of matches
// use the g flag with the regex.
// i.e. /pattern/g.

// Note: You can use multiple flags by concatenating them.

let twinkleStar = "Twinkle, twinkle, little star";
let starRegex = /Twinkle/gi; // Change this line
let result = twinkleStar.match(starRegex); // Change this line

console.log(result);
