#!/usr/bin/node
let argnumber = process.argv.length - 2;
if (argnumber < 1) {
  console.log('No argument');
} else if (argnumber === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
