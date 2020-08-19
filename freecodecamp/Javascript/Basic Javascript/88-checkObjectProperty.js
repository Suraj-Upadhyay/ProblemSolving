// You can check whether a property exists for an object or not
// by using hasOwnProperty(propname).

function checkObj(obj, checkProp) {
    // Only change code below this line
    if (obj.hasOwnProperty(checkProp)) {
      return obj[checkProp];
    }
    return "Not Found";
    // Only change code above this line
}
