// Examples.
const getMousePosition = (x, y) => ({
  x: x,
  y: y
});

// In ES6, the above code can be rewritten as

const getMousePosition = (x, y) => ({ x, y });

// The challenge.
const createPerson = (name, age, gender) => {
  "use strict";
  // Only change code below this line
  return {name, age, gender};
  // Only change code above this line
};
