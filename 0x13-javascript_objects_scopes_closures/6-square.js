#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/* Instance method called charPrint(c) that prints the rectangle
using the character c */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let string1 = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          string1 += 'X';
        } else {
          string1 += 'C';
        }
      }
      if (i + 1 !== this.height) {
        string1 += '\n';
      }
    }
    console.log(string1);
  }
}
module.exports = Square;
