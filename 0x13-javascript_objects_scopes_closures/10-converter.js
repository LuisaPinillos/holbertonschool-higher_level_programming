#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (num)
  {
    let numconvert = num.toString(base)
    return (numconvert);
  }
}
