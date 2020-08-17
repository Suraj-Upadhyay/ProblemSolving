/* The equality (==) operator when evaluating an expression converts
   both the operands to a common type.
   The strict equality (===) operator doesn't do that and returns true
   only if the operands are of same type and are equal.
*/

// Setup
function testStrict(val) {
    if (val === 7) { // Change this line
      return "Equal";
    }
    return "Not Equal";
}

testStrict(10);  
