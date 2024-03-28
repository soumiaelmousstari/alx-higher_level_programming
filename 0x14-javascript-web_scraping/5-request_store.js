#!/usr/bin/node

const request = require('request');
const fisy = require('fs');

request(process.argv[2], function (_err, _res, body) {
  fisy.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
