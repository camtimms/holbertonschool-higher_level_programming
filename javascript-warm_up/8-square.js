#!/usr/bin/node

const args = process.argv.slice(2);
const square_size = parseInt(args[0]);

if (isNaN(square_size)) {
  console.log('Missing size')
} else {
  for (let i = 0; i < square_size; i++) {
    let row = '';
  for (let j = 0; j < square_size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}