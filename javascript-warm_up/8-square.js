#!/usr/bin/node

const args = process.argv.slice(2);
const squareSize = parseInt(args[0]);

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    let row = '';
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
