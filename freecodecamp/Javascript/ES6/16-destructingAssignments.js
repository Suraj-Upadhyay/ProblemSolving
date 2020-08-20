// You can perform destruction of objects and array inside
// a function's paramters list too, saves a few lines.

const stats = {
  max: 56.78,
  standard_deviation: 4.34,
  median: 34.54,
  mode: 23.87,
  min: -0.75,
  average: 35.85
};

// Only change code below this line
const half = ({max, min}) => (max + min) / 2.0; 
// Only change code above this line

// Here the stats object is destructed into max and min in the function half.
console.log(half(stats));
