#!/usr/bin/node
let string = process.argv[2];
if (string === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
