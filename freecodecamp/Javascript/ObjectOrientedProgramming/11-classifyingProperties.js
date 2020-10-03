function Dog(name) {
    this.name = name;
}

Dog.prototype.numLegs = 4;

let beagle = new Dog("Snoopy");

let ownProps = [];
let prototypeProps = [];

// Only change code below this line

for (let properties in beagle) {
if (beagle.hasOwnProperty(properties))
    ownProps.push(properties);
else
    prototypeProps.push(properties);
}

console.log(ownProps);
console.log(prototypeProps);
