function titleCase(str) {
    let newStr = '';
    for (let i = 0; i < str.length; i++) {
      let j = i;
      for (; j < str.length && str[j] != ' '; j++);
      newStr += str[i].toUpperCase() + str.slice(i + 1, j + 1).toLowerCase();
      i = j;
    }
    return newStr;
}

console.log(titleCase("I'm a little tea pot"));
