let users = {
    Alan: {
      age: 27,
      online: true
    },
    Jeff: {
      age: 32,
      online: true
    },
    Sarah: {
      age: 48,
      online: true
    },
    Ryan: {
      age: 19,
      online: true
    }
};

function isEveryoneHere(obj) {
    // Only change code below this line
    let keys = ['Alan', 'Jeff', 'Sarah', 'Ryan']
    for (let i = 0; i < 4; i++) {
      if (!obj.hasOwnProperty(keys[i]))
        return false;
    }
    return true;
    // Only change code above this line
}

console.log(isEveryoneHere(users));
