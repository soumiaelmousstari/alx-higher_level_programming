#!/usr/bin/node

const request = require('request');
let ind = 0;

request(process.argv[2], function (error, response, body) {
  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        ind += 1;
      }
    }
  }

  console.log(ind);
});
