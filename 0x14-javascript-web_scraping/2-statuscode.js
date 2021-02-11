#!/usr/bin/node
let request = require('request');
let rl = process.argv[2];
request(rl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
