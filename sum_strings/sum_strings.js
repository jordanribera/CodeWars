function sumStrings(a,b) {
  if (a == "") a = "0";
  if (b == "") b = "0";
  a = a.replace(/\b0+/g, '');
  b = b.replace(/\b0+/g, '');
  aArray = a.split("").reverse();
  bArray = b.split("").reverse();
  cArray = new Array(Math.max(aArray.length, bArray.length) + 1);
  for (i = 0; i < cArray.length; i++) cArray[i] = '0';
  answerArray = new Array(cArray.length);
  for (var x = 0; x < (cArray.length - 1); x++)
  {
    placeSum = parseInt(cArray[x]);
    if (x < aArray.length) placeSum += parseInt(aArray[x]);
    if (x < bArray.length) placeSum += parseInt(bArray[x]);
    carryValue = placeSum -(placeSum % 10);
    placeSum = placeSum % 10;
    answerArray[x] = placeSum;
    cArray[x + 1] = "" + (carryValue / 10);
  }
  if (cArray[cArray.length - 1] != '0') answerArray.push(cArray[cArray.length - 1]);
  return answerArray.reverse().join('')
}
