// Like the equality operator, this changes the operands into common type.

// Setup
function testNotEqual(val) {
    if (val != 99) { // Change this line
      return "Not Equal";
    }
    return "Equal";
}

testNotEqual(10);
