function factorialize(num) {
    return num == 0 ? 1: num * factorialize(num - 1);
}

console.log(factorialize(5));
