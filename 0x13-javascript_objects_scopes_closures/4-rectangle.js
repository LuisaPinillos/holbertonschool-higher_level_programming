#!/usr/bin/node

/* Instance method called rotate() that exchange the width and height
and the method double that mulpiplies the height and width per 2. */


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

  rotate () {
    const saveheight = this.width;
    this.width = this.height;
    this.height = saveheight;
    return (this.width, this.height);
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
    return (this.width, this.height);
  }
}
module.exports = Rectangle;
