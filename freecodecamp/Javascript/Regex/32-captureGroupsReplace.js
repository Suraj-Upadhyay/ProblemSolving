// Regex allows you to replace the sub-string(s) matched.
// And capture groups come very handy in such modifications or replacements
// due to them being numerable.

// E.g.

let wrongText = "The sky is silver.";
let silverRegex = /silver/;
wrongText.replace(silverRegex, "blue");

// E.g.

// You can access capture groups in replacement strings with dollar signs.
"Code Camp".replace(/(\w+)\s(\w+)/, '$2 $1');

// Challenge.
// i/p - "one two three" o/p - "three two one"
let str = "one two three";
let fixRegex = /(\w+) (\w+) (\w+)/;
let replaceText = "$3 $2 $1"; // Change this line
let result = str.replace(fixRegex, replaceText);

console.log(result);

