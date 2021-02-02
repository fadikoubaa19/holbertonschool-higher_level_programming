#!/usr/bin/node
let ali = process.argv.length - 2;
if (ali < 1) {
  console.log('No argument');
} else if (ali === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
