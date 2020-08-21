// Quantity Specifiers have two quantities for lower and upper limit
// inside curly brackets.
// for e.g. /a{3, 5}h/ which would match patterns with 3 to 4 a(s) followed by an h.

let ohStr = "Ohhh no";
// Do not put any spaces after the comma in the quantity specifier.
let ohRegex = /Oh{3,6} no/; // Change this line
let result = ohRegex.test(ohStr);
