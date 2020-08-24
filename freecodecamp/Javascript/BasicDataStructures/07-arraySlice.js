// The slice method extracts and returns elements from an array.
// It doesn't modify the original array.
// The method takes two arguments, say, i and j and extracts elements
// between i (including) and j (excluding).

function forecast(arr) {
    // Only change code below this line
    return arr.slice(2, 4);
}

// Only change code above this line
console.log(forecast(['cold', 'rainy', 'warm', 'sunny', 'cool', 'thunderstorms']));
// Outputs : ['warm', 'sunny']
