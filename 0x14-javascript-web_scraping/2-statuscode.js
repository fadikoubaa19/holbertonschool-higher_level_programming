#!/usr/bin/node
const request = require('request');
const rl = process.argv[2];
request(rl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
