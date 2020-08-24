function countOnline(usersObj) {
    // Only change code below this line
    let count = 0;
    for (let users in usersObj) {
      if (usersObj[users].online)
        count ++;
    }
    return count;
    // Only change code above this line
}
