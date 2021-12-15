#!/usr/bin/node

exports.converter = function (base) {
  return function myConverter (num) {
    const numconvert = num.toString(base);
    return (numconvert);
  };
};
