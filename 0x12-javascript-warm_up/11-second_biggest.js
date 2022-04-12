#!/usr/bin/node

// Script that searches the second biggest integer in the list of arguments.
const list_Args = process.argv.length;
if (list_Args > 3) {
  const list_order = process.argv.sort();
  const sec_max = list_order.reverse()[1];
  console.log(sec_max);
} else {
  console.log(0);
}
