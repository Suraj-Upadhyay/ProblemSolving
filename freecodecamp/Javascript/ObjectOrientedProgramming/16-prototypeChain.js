// All objects in javascript (with a few exceptions) have prototypes.
// A prototype is itself an object, and thus it can have its own prototype.
// In the example given below, the prototype of Dog.prototype is Object.prototype.
// The hasOwnProperty is actually in the prototype of the objects.

function Dog(name) {
    this.name = name;
}

let beagle = new Dog("Snoopy");

Dog.prototype.isPrototypeOf(beagle);  // yields true

// Fix the code below so that it evaluates to true
console.log(Object.prototype.isPrototypeOf(Dog.prototype));
