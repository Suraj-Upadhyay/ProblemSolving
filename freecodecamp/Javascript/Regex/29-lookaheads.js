// Lookaheads are patterns that tell javascript to look ahead in your string
// to check for patterns further along.
// Positive and negative lookaheads are respectively (?=...) and (?!...) where
// the three-dots are patterns to be searched.
// Positive lookahead seeks for existence and negative lookahead seeks for absence.

let sampleWord = "astronaut";
// Check for password with more than 5 characters, beginning with a non-number and
// containing two consecutive numbers.
let pwRegex = /(?=\w{6,})(?=^\D\w*\d{2}\w*)/;
let result = pwRegex.test(sampleWord);

console.log(result);

