#!/usr/bin/node

// Script that prints a square.
let j = 0;
while (j < process.argv.length) {
  j++;
}
if (j === 1) {
  console.log('Missing size');
} else {
  if (parseInt(process.argv[2])) {
    if (parseInt(process.argv[2]) > 0) {
      let string1 = '';
      for (let i = 0; i < parseInt(process.argv[2]); i++) {
        for (let a = 0; a < parseInt(process.argv[2]); a++) {
          string1 += 'X';
        }
        if (i + 1 !== parseInt(process.argv[2])) {
          string1 += '\n';
        }
      }
      console.log(string1);
    }
  } else {
    console.log('Missing size');
  }
}
