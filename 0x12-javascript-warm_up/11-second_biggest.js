#!/usr/bin/node

// Script that searches the second biggest integer in the list of arguments.

const listArgs = process.argv.length;

if (listArgs <= 3) {
  console.log(0);
} else {
  const listOrder = process.argv.sort();
  const secMax = listOrder.reverse()[1];
  console.log(secMax);
}
