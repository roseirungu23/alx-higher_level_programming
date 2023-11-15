#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let y = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      y += 1;
    }
  }
  return y;
};
