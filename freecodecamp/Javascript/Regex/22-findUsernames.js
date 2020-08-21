let username = "JackOfAllTrades";

// Either find a username with two or more leading letters
// and zero or more numbers at the end.
// or find a username with leading one or more letters and
// two or more numbers.
let userCheck = /^[a-z][a-z]+\d*$|^[a-z]+\d\d+$/i;
let result = userCheck.test(username);

console.log(result);
