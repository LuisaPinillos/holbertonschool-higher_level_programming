#!/usr/bin/node

// If w or h is equal to 0 or not a positive integer, create an empty object.

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      // empty
    } else {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
