#!/usr/bin/node

// Update this script to replace the value 12 with 89.

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

if (myObject.value === 12) {
  myObject.value = 89;
}
console.log(myObject);
