#!/usr/bin/node
let ag = process.argv[2];
if (ag === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
