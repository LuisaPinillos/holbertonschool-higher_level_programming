#!/usr/bin/node

// conditions for the number of arguments.
let i;

for (i = 2; i < process.argv.length; i++);
if (i === 2) {
  console.log('No argument');
} else if (i === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
