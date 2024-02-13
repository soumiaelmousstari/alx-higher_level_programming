#!/usr/bin/node
const nbr = Math.floor(Number(process.argv[2]));
if (isNaN(nbr)) {
  console.log(1);
} else {
  let j;
  j = 1;
  for (let i = 1; i <= nbr; i++) {
    j *= i;
  }
  console.log(j);
}
