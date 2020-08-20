// To export parts of your code i.e. functions, objects or data
// you can use the keyword `export` with the code to be exported.
// for e.g.

export const add = (x, y) => {
  return x + y;
}
// The alternative to preceeding every declaration with export keyword
// is using a parenthesis with the export keyword to include everything
// to be exported in a comma seperated sequence.
export { add,  subtract , ...};

// Challenge.

const uppercaseString = (string) => {
  return string.toUpperCase();
}

const lowercaseString = (string) => {
  return string.toLowerCase()
}

export {uppercaseString, lowercaseString};
