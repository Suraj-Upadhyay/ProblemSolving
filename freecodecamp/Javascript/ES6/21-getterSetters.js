// To access and modify private properties of an object,
// we use getters (to access data) and setters (to modify data).
// By convention you should preceed variables meant to be private with '_'.
// Here is the syntax to do so.
class Book {
  constructor(author) {
    this._author = author;
  }
  // getter
  get writer() {
    return this._author;
  }
  // setter
  set writer(updatedAuthor) {
    this._author = updatedAuthor;
  }
}
const lol = new Book('anonymous');
// The call to setters and getters don't even look like a normal function call.
console.log(lol.writer);  // anonymous
lol.writer = 'wut';
console.log(lol.writer);  // wut

// Challenge.

// Only change code below this line
// Store the temperature in fehrenheit with a celsius getter and setter.
class Thermostat {
  constructor(temp) {
    this._temp = temp;
  }
  get temperature() {
    return (this._temp - 32) * 5 / 9;
  }
  set temperature(temp) {
    this._temp = temp * 9.0 / 5 + 32;
  }
}
// Only change code above this line

const thermos = new Thermostat(76); // Setting in Fahrenheit scale
let temp = thermos.temperature; // 24.44 in Celsius
thermos.temperature = 26;
temp = thermos.temperature; // 26 in Celsius
