#!/usr/bin/node
const nbrarg = process.argv.length - 2;
console.log(nbrarg === 0 ? 'No argument' : nbrarg === 1 ? 'Argument found' : 'Arguments found');
