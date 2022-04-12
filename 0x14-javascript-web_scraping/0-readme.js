#!/usr/bin/node

// Script that reads and prints the content of a file.

const myFile = process.argv[2];
// Requiring fs module in which
// readFile function is defined.
const fs = require('fs');

fs.readFile(myFile, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
