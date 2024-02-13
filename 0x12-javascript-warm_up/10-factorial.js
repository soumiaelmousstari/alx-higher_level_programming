#!/usr/bin/node
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  return (a * factorial(--a));
}
const nbr = Math.floor(Number(process.argv[2]));
if (isNaN(nbr)) {
  console.log(1);
} else {
  console.log(factorial(nbr));
}
