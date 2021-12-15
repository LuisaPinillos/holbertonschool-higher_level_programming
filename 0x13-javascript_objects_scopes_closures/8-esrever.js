#!/usr/bin/node

/* Function that returns the reversed version of a list. */

exports.esrever = function (list) {
  const listrev = [];
  for (let i = list.length - 1; i >= 0; i--) {
    listrev.push(list[i]);
  }
  return listrev;
};
