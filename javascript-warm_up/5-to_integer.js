#!/usr/bin/node

const args = process.argv.slice(2);

try {
  const num = parseInt(args[0]);

  if (isNaN(num)) {
    throw new Error('Invalid number')
  }
  console.log(`My number: ${num}`)
}
catch (error) {
  console.log('Not a number')
}
