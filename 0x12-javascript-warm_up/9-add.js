#!/usr/bin/node
function add (a, b) {
  return (a + b);
}
const nbr1 = Math.floor(Number(process.argv[2]));
const nbr2 = Math.floor(Number(process.argv[3]));
if (isNaN(nbr1) || isNaN(nbr2)) {
  console.log('NaN');
} else {
  console.log(`${add(nbr1, nbr2)}`);
}
