function Bird(name) {
    this.name = name;
    this.numLegs = 2;
}

let canary = new Bird("Tweety");
let ownProps = [];
// Only change code below this line

for (let ownProperty in canary) {
if (canary.hasOwnProperty(ownProperty))
    ownProps.push(ownProperty);
}

console.log(ownProps);
