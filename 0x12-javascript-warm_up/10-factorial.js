#!/usr/bin/node

// Script that computes and prints a factorial.

function factorial (a) {
  let fact = 1;
  for (let i = 1; i <= a; i++) {
    fact *= i;
  }
  console.log(fact);
}
factorial(parseInt(process.argv[2]));
