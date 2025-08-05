#!/usr/bin/node

const args = process.argv.slice(2);

let largest = 0;
let prevLargest = 0;

if (args.length <= 1) {
  console.log(0);
} else {
  for (const arg of args) {
    const num = parseInt(arg);

    if (num > largest) {
      prevLargest = largest;
      largest = num;
    } else if (num > prevLargest && num < largest) {
      prevLargest = num;
    }
  }
  console.log(prevLargest);
}

