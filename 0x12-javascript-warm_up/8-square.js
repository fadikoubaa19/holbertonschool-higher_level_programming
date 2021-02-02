#!/usr/bin/node
let xxx = process.argv[2];
if (isNaN(xxx)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < xxx; i++) {
    console.log('X'.repeat(xxx));
  }
}
