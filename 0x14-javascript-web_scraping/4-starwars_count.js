#!/usr/bin/node
const request = require('request');
const rl = process.argv[2];
request(rl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const filmList = JSON.parse(body).results;
    let count = 0;
    for (const film in filmList) {
      const charList = filmList[film].characters;
      for (const character in charList) {
        if (charList[character].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Wrong status code');
  }
});
