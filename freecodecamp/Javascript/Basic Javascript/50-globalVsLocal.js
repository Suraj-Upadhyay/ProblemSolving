/* A local variable with same name as a global variable has higher
   precedence than the global variable.
 */

// Setup
var outerWear = "T-Shirt";

function myOutfit() {
  // Only change code below this line
  var outerWear = 'sweater';
  // Only change code above this line
  return outerWear;
}

myOutfit();
