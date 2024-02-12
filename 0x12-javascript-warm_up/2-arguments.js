#!/usr/bin/node
const nbr_arg = process.argv.length - 2;
console.log(nbr_arg === 0 ? 'No argument' : nbr_arg === 1 ? 'Argument found' : 'Arguments found');
