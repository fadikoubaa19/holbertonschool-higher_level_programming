#!/usr/bin/node
exports.esrever = function (list) {
  const newone = [];
  for (let i = 0; i < list.length; i++) {
    newone.unshift(list[i]);
  }
  return newone;
};
