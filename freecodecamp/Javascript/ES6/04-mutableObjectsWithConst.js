// Mutable objects can still be changes without it's pointing identifier
// being modified, for e.g. if an array is held by a const variable,
// it can still be modified with push, shift, etc. functions.

const s = [5, 7, 2];

function editInPlace() {
  'use strict';
  // Only change code below this line

  // Using s = [2, 5, 7] would be invalid
  s.push(s.shift());
  s.push(s.shift());
  // Only change code above this line
}

editInPlace();
console.log(s);
