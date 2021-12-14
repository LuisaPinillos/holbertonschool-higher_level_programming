#!/usr/bin/node

// prints the first argument passed to it.

let i = 2;

while (process.argv[i]) {
  i++;
}
if (i === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
