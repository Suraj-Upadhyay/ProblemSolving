// Remove any number of consecutive elements with the splice method.
// splice takes three arguments.
// The first is the index of any element whence the deletion is done.
// The second argument is the number of elements that will be deleted
// including the starting element.

// Modifies the original array.
// Returns an array containing removed elements.

const arr = [2, 4, 5, 1, 7, 5, 2, 1];
// Only change code below this line
arr.splice(1, 4); // delete 4 elements from and including element at index 1.
// Only change code above this line
console.log(arr);
