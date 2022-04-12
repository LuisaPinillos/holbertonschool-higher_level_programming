#!/usr/bin/node

// Script that searches the second biggest integer in the list of arguments.
let list_Args = process.argv.length;
if (list_Args > 3) {
  const list_order = process.argv.sort();
  const num_max = process.argv[list_Args - 2];
  console.log(num_max);
}
else {
  console.log(0);
}
