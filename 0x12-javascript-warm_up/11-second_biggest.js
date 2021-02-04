#!/usr/bin/node
const process = require('process');
let extrass = 0;
let l = 0;
for (let i = 2; parseInt(process.argv[i]); i++) {
  if (parseInt(process.argv[i]) > extrass){
      extrass=process.argv[i];
}}
console.log(extrass)
