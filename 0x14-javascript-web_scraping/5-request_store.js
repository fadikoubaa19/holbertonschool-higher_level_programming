#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const rl = process.argv[2];
const file = process.argv[3];
request(rl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log('Wrong status code');
  }
});
