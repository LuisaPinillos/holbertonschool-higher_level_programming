#!/usr/bin/node

// Script that computes and prints a factorial.

if (parseInt(process.argv[2])) {
  let fact = 1;
  for (let i = 1; i <= parseInt(process.argv[2]); i++) {
    fact *= i;
  }
  console.log(fact);
} else {
  console.log(1);
}
