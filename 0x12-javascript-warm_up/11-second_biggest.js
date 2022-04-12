#!/usr/bin/node

// Script that searches the second biggest integer in the list of arguments.

const listArgs = process.argv.length;

if (listArgs >= 2) {
  const listOrder = process.argv.sort();
  const secMax = listOrder.reverse()[1];
  console.log(secMax);
} else {
  console.log(0);
}
