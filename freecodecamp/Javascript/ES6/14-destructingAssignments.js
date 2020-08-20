// Examples of destructing arrays into variables.

const [a, b] = [1, 2, 3, 4, 5, 6];
console.log(a, b); // 1, 2

const [a, b,,, c] = [1, 2, 3, 4, 5, 6];
console.log(a, b, c); // 1, 2, 5

// The actual challenge.

let a = 8, b = 6;
// Only change code below this line
[a, b] = [b, a]

console.log(a, b); // 6, 8
