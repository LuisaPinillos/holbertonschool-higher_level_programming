#!/usr/bin/node

//prints the number of arguments already printed and the new argument value.

let countarg = 0;
exports.logMe = function (item) {
  console.log(countarg + ': ' + item);
  countarg += 1;
};
