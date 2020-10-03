// Properties in the prototype are shared among ALL instances of the object.

function Dog(name) {
    this.name = name;
}

Dog.prototype.numLegs = 4;

// Only change code above this line
let beagle = new Dog("Snoopy");

console.log(beagle.numLegs); // => 4;
