// Using `?` after a pattern implies either its full existence or absence.

let favWord = "favorite";
let favRegex = /favou?rite/; // Change this line
let result = favRegex.test(favWord);
