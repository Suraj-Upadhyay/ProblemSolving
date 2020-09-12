function repeatStringNumTimes(str, num) {
    let ret = "";
    for (;num > 0; num--)
      ret += str;
    return ret;
}

console.log(repeatStringNumTimes("abc", 3));
