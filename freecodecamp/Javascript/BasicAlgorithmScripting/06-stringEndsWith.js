function confirmEnding(str, target) {
    return str.substring(str.length - target.length, str.length) == target;
}

console.log(confirmEnding("Bastian", "n"));
