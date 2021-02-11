#!/usr/bin/node
const request = require('request');
const rl = 'http://swapi.co/api/films/:id';
const episodeNumber = process.argv[2];
request(rl + episodeNumber, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Wrong status code');
  }
});
