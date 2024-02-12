#!/usr/bin/node
const nbr_arg = process.argv.length;
if (nbr_arg == 0)
	console.log('No argument');
else if (nbr_arg == 1)
	console.log('Argument found');
else
	console.log('Arguments found');
