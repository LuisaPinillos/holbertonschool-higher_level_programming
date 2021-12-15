#!/usr/bin/node

// prints 3 lines with a loop.
let i = 0;
let j = 0;
while (j < process.argv.length) {
  j++;
}
if (j === 2) {
  console.log('Missing number of occurrences');
} else {
  const x = process.argv[2];
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
