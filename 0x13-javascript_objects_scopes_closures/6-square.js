#!/usr/bin/node

/* Instance method called charPrint(c) that prints the rectangle
using the character c */

class Square extends require('./5-square') {
  charPrint (c) {
    c = c || 'X';
    let string1 = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string1 += c;
      }
      if (i + 1 !== this.height) {
        string1 += '\n';
      }
    }
    console.log(string1);
  }
}
module.exports = Square;
