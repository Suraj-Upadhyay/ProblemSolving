let waldoIsHiding = "Somewhere Waldo is hiding in this text.";

// The Regex in this form just matches the string "Waldo"
// in a case-sesitive manner.
let waldoRegex = /Waldo/; // Change this line

let result = waldoRegex.test(waldoIsHiding);
