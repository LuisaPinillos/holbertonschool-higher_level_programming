#!/usr/bin/node

// Script that writes a string to a file.

const myFile = process.argv[2];
const theData = process.argv[3];
const fs = require('fs');
fs.writeFile(myFile, theData, 'utf-8', function (err) {
  if (err) {
    return console.log(err);
  }
});
