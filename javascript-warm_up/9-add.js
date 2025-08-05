#!/usr/bin/node

const args = process.argv.slice(2);
const num1 = args[0];
const num2 = args[1];

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return (a + b);
}

console.log(add(num1, num2));
