#!/usr/bin/node
const nbr = Math.floor(Number(process.argv[2]));
if (isNaN(nbr)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < nbr; i++) {
    let str = '';
    for (let j = 0; j < nbr; j++) {
      str += 'X';
    }
    console.log(str);
  }
}
