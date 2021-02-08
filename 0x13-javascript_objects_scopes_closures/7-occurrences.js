#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let total = 0;
  for (let i in list) {
    if (list[i] === searchElement) {
      total++;
    }
  }
  return total;
};
