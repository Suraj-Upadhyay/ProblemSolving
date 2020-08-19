var count = 0;

function cc(card) {
  // Only change code below this line
  var change = -1;
  var str;
  if (card > 1 && card < 7) {
    change = 1;
  } else if (card < 10) {
    change = 0;
  }
  count += change;
  if (count > 0) {
    str = "Bet";
  } else {
    str = "Hold";
  }
  return count + ' ' + str;
  // Only change code above this line
}

cc(2); cc(3); cc(7); cc('K'); cc('A');
