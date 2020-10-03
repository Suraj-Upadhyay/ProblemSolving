// The private variables are defined normally with the let keyword
// and cannot be accessed by the methods outside the constructor.

function Bird() {
    let weight = 15; // A private variable
    this.getWeight = function() {   
      return weight;
    };
}

let bird = new Bird();
console.log(bird.getWeight());
