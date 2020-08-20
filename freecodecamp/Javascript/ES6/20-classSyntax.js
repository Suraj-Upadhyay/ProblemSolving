// The ECMAScrypt just provides for a class syntax and
// doesn't have the full object-oriented infrastructure like
// other languages such as python, java, c++, etc.

// This class syntax is used for declaring function to which
// a constructor is added. This contructor is called when
// new is used to create a new object.

// Only change code below this line
// The class names should be in UpperCamelCase.
class Vegetable {
  constructor(nameString) {
    this.name = nameString;
  }
}
// Only change code above this line

const carrot = new Vegetable('carrot');
console.log(carrot.name); // Should display 'carrot'
