#!/usr/bin/node

// instance method called print() that prints the rectangle using the character X.

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // empty
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let string1 = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        string1 += 'X';
      }
      if (i + 1 !== this.height) {
        string1 += '\n';
      }
    }
    console.log(string1);
  }
}
module.exports = Rectangle;
