// Capture groups are regex patterns within ().
// These can be referred to later in regex by numbering their occurence
// like \1, \2, \3, \4 ,... .  Thus preventing manual repeatition of patterns.

// The below regex matches a string containing a number repeated three times
// and separated by spaces.
let repeatNum = "42 42 42";
let reRegex = /^(\d+)\s\1\s\1$/; // Change this line
let result = reRegex.test(repeatNum);

console.log(result);
