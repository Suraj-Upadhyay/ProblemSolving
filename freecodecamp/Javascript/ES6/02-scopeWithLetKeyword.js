// The scope of the variable declared by the `let` keyword is
// the nearest enclosing brackets, statement or expression 
// or the has the global scope if declared outside of any functions.

// With the `var` keyword it was either a function's scope or global scope.

function checkScope() {
    'use strict';
    let i = 'function scope';
    if (true) {
      let i = 'block scope';
      console.log('Block scope i is: ', i);
    }
    console.log('Function scope i is: ', i);
    return i;
}

checkScope();
