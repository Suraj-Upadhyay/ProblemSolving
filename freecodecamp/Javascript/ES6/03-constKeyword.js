// Declaring variables with `const` keyword isn't any different than
// the `let` keyword except the const variables are read-only i.e. 
// the variable identifier cannot be reassigned.

function printManyTimes(str) {
    "use strict";
    // Only change code below this line
    const SENTENCE = str + " is cool!";
    for (let i = 0; i < str.length; i+=2) {
      console.log(SENTENCE);
    }
    // Only change code above this line
}

printManyTimes("freeCodeCamp");
