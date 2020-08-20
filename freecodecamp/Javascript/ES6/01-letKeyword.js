// The problem with using `var` keyword for declaring variables is that
// you can override a variable declaration without having an error.
// To solve this issue es6 introduced a new keyword `let` to declare variables.

let catName;
let quote;
function catTalk() {
  "use strict";

  catName = "Oliver";
  quote = catName + " says Meow!";

}

catTalk();
